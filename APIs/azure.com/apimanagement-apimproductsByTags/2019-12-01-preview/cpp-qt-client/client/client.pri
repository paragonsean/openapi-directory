QT += network

HEADERS += \
# Models
    $${PWD}/OAIProduct_ListByTags_200_response.h \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner.h \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_api.h \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_operation.h \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_product.h \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_tag.h \
    $${PWD}/OAIProduct_ListByTags_default_response.h \
    $${PWD}/OAIProduct_ListByTags_default_response_error.h \
    $${PWD}/OAIProduct_ListByTags_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIProductsByTagApi.h \
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
    $${PWD}/OAIProduct_ListByTags_200_response.cpp \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner.cpp \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_api.cpp \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_operation.cpp \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_product.cpp \
    $${PWD}/OAIProduct_ListByTags_200_response_value_inner_tag.cpp \
    $${PWD}/OAIProduct_ListByTags_default_response.cpp \
    $${PWD}/OAIProduct_ListByTags_default_response_error.cpp \
    $${PWD}/OAIProduct_ListByTags_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIProductsByTagApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
