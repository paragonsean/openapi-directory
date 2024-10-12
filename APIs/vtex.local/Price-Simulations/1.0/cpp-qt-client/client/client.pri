QT += network

HEADERS += \
# Models
    $${PWD}/OAICustomSessionKeys.h \
    $${PWD}/OAIFields_inner.h \
    $${PWD}/OAIPublic.h \
    $${PWD}/OAIRequest_Body.h \
    $${PWD}/OAIRequest_body.h \
    $${PWD}/OAIRequest_body_1.h \
    $${PWD}/OAI__v_custom_prices_rules_post_200_response.h \
    $${PWD}/OAI__v_custom_prices_rules_post_request.h \
# APIs
    $${PWD}/OAICustomPricesApi.h \
    $${PWD}/OAIPriceAssociationApi.h \
    $${PWD}/OAISessionManagementApi.h \
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
    $${PWD}/OAICustomSessionKeys.cpp \
    $${PWD}/OAIFields_inner.cpp \
    $${PWD}/OAIPublic.cpp \
    $${PWD}/OAIRequest_Body.cpp \
    $${PWD}/OAIRequest_body.cpp \
    $${PWD}/OAIRequest_body_1.cpp \
    $${PWD}/OAI__v_custom_prices_rules_post_200_response.cpp \
    $${PWD}/OAI__v_custom_prices_rules_post_request.cpp \
# APIs
    $${PWD}/OAICustomPricesApi.cpp \
    $${PWD}/OAIPriceAssociationApi.cpp \
    $${PWD}/OAISessionManagementApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
