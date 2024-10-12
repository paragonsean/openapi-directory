QT += network

HEADERS += \
# Models
    $${PWD}/OAIApi_ListByTags_200_response.h \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner.h \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_api.h \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_operation.h \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_product.h \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_tag.h \
    $${PWD}/OAIApi_ListByTags_default_response.h \
    $${PWD}/OAIApi_ListByTags_default_response_error.h \
    $${PWD}/OAIApi_ListByTags_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIApisByTagApi.h \
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
    $${PWD}/OAIApi_ListByTags_200_response.cpp \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner.cpp \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_api.cpp \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_operation.cpp \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_product.cpp \
    $${PWD}/OAIApi_ListByTags_200_response_value_inner_tag.cpp \
    $${PWD}/OAIApi_ListByTags_default_response.cpp \
    $${PWD}/OAIApi_ListByTags_default_response_error.cpp \
    $${PWD}/OAIApi_ListByTags_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIApisByTagApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
