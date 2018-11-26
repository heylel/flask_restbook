from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    # 参数校验规则：
    # 1.定义的属性名q,page要与要校验的参数同名
    # 2.根据要传入的参数类型选择不同的Field类进行实例化
    # 3.传入一个数组，作为校验规则validators
    # 4.可以设置默认值
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message="查询关键字长度必须在1-30之间")], )
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
