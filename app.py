from flask import Flask, render_template, request, redirect, url_for, session
import flask_sqlalchemy
import os

app = Flask(__name__)
app.secret_key = 'coffee_secret_key' # لتفعيل الجلسات (Sessions)

#  قاعدة البيانات
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'coffee_shop.db')
db = flask_sqlalchemy.SQLAlchemy(app)

#  جدول المستخدم و العدادات
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    # العدادات الجديدة (تبدأ من الصفر)
    ethiopian_count = db.Column(db.Integer, default=0)
    colombian_count = db.Column(db.Integer, default=0)
    yemeni_count = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        # حفظ رقم تعريف المستخدم في "الجلسة" لنتبعه في الصفحات القادمة
        session['user_id'] = new_user.id 
        return redirect(url_for('products_list'))
    return render_template('register.html')

@app.route('/products')
def products_list():
    return render_template('products.html')

@app.route('/product/ethiopian')
def ethiopian_page():
    return render_template('ethiopian.html')

@app.route('/product/colombian')
def colombian_page():
    return render_template('colombian.html')

@app.route('/product/yemeni')
def yemeni_page():
    return render_template('yemeni.html')

# صفحة من نحن
@app.route('/about')
def about_page():
    return render_template('about.html')

# المسار الجديد والمطور للسلة (لقبول اسم المحصول ويحفظه ثم يوجهك لصفحة السلة)
@app.route('/add_to_cart/<coffee_type>')
def add_to_cart(coffee_type):
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if coffee_type == 'ethiopian':
            user.ethiopian_count += 1
        elif coffee_type == 'colombian':
            user.colombian_count += 1
        elif coffee_type == 'yemeni':
            user.yemeni_count += 1
        
        db.session.commit()
    
    # التحويل مباشرة لمسار السلة لاستعراض المنتجات
    return redirect(url_for('cart'))

# مسار صفحة السلة 
@app.route('/cart')
def cart():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('register')) # إعادة للرئيسية إذا لم يسجل دخول
        
    user = User.query.get(user_id)
    cart_items = []
    total_price = 0
    
    # التحقق من العدادات وإضافتها للسلة إذا كانت أكثر من صفر
    if user.yemeni_count > 0:
        total_item_price = user.yemeni_count * 85
        cart_items.append({'name': 'قهوة يمنية - حرازي', 'qty': user.yemeni_count, 'price': total_item_price})
        total_price += total_item_price
        
    if user.ethiopian_count > 0:
        total_item_price = user.ethiopian_count * 65
        cart_items.append({'name': 'قهوة إثيوبية - يورغاشيف', 'qty': user.ethiopian_count, 'price': total_item_price})
        total_price += total_item_price
        
    if user.colombian_count > 0:
        total_item_price = user.colombian_count * 75
        cart_items.append({'name': 'قهوة كولومبية', 'qty': user.colombian_count, 'price': total_item_price})
        total_price += total_item_price

    # عرض قالب السلة وتمرير البيانات الحقيقية المحسوبة
    return render_template('cart.html', cart_items=cart_items, total=total_price)

#  لتشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)
