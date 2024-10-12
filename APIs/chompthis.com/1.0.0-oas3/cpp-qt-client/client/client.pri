QT += network

HEADERS += \
# Models
    $${PWD}/OAIBrandedFoodObject.h \
    $${PWD}/OAIBrandedFoodObject_items_inner.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_country_details.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_flags_inner.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_gluten_free.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_vegan.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_vegetarian.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_nutrients_inner.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_package.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_front.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_ingredients.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_nutrition.h \
    $${PWD}/OAIBrandedFoodObject_items_inner_serving.h \
    $${PWD}/OAIIngredientObject.h \
    $${PWD}/OAIIngredientObject_items_inner.h \
    $${PWD}/OAIIngredientObject_items_inner_calorie_conversion_factor.h \
    $${PWD}/OAIIngredientObject_items_inner_components_inner.h \
    $${PWD}/OAIIngredientObject_items_inner_nutrients_inner.h \
    $${PWD}/OAIIngredientObject_items_inner_portions_inner.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIBrandedFoodObject.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_country_details.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_flags_inner.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_gluten_free.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_vegan.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_diet_labels_vegetarian.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_nutrients_inner.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_package.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_front.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_ingredients.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_packaging_photos_nutrition.cpp \
    $${PWD}/OAIBrandedFoodObject_items_inner_serving.cpp \
    $${PWD}/OAIIngredientObject.cpp \
    $${PWD}/OAIIngredientObject_items_inner.cpp \
    $${PWD}/OAIIngredientObject_items_inner_calorie_conversion_factor.cpp \
    $${PWD}/OAIIngredientObject_items_inner_components_inner.cpp \
    $${PWD}/OAIIngredientObject_items_inner_nutrients_inner.cpp \
    $${PWD}/OAIIngredientObject_items_inner_portions_inner.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
