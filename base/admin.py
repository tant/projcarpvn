from django.contrib import admin
from django.apps import apps

# Tạm viết vầy cho nhanh nhưng sau đó sẽ đổi lại kiểu add từng module thủ công cho sạch giao diện

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
