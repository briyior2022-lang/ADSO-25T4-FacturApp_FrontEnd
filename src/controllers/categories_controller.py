from flask import Blueprint, render_template

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/form_categories')
def form_categories():
    return render_template('categories/form_categories.html')

@categories_bp.route('/list_categories')
def list_categories():
    return render_template('/categories/list_categories.html')


    from flask import Blueprint, render_template

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
def listar_productos():
    # Aquí luego conectarás la consulta a MySQL
    return render_template('productos/list_productos.html')