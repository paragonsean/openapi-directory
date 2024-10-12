QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAsset_urls.h \
    $${PWD}/OAIAttachment.h \
    $${PWD}/OAIAuthorized_payment_method.h \
    $${PWD}/OAICreate_order_request.h \
    $${PWD}/OAICustomer.h \
    $${PWD}/OAICustomer_read.h \
    $${PWD}/OAICustomer_read_create_token.h \
    $${PWD}/OAICustomer_token_creation_request.h \
    $${PWD}/OAICustomer_token_creation_response.h \
    $${PWD}/OAIErrorV2.h \
    $${PWD}/OAIMerchant_session.h \
    $${PWD}/OAIMerchant_urls.h \
    $${PWD}/OAIOptions.h \
    $${PWD}/OAIOrder.h \
    $${PWD}/OAIOrder_line.h \
    $${PWD}/OAIPayment_method_category.h \
    $${PWD}/OAIProduct_identifiers.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAISession_create.h \
    $${PWD}/OAISession_read.h \
    $${PWD}/OAISubscription.h \
# APIs
    $${PWD}/OAIOrdersApi.h \
    $${PWD}/OAISessionsApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAsset_urls.cpp \
    $${PWD}/OAIAttachment.cpp \
    $${PWD}/OAIAuthorized_payment_method.cpp \
    $${PWD}/OAICreate_order_request.cpp \
    $${PWD}/OAICustomer.cpp \
    $${PWD}/OAICustomer_read.cpp \
    $${PWD}/OAICustomer_read_create_token.cpp \
    $${PWD}/OAICustomer_token_creation_request.cpp \
    $${PWD}/OAICustomer_token_creation_response.cpp \
    $${PWD}/OAIErrorV2.cpp \
    $${PWD}/OAIMerchant_session.cpp \
    $${PWD}/OAIMerchant_urls.cpp \
    $${PWD}/OAIOptions.cpp \
    $${PWD}/OAIOrder.cpp \
    $${PWD}/OAIOrder_line.cpp \
    $${PWD}/OAIPayment_method_category.cpp \
    $${PWD}/OAIProduct_identifiers.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAISession_create.cpp \
    $${PWD}/OAISession_read.cpp \
    $${PWD}/OAISubscription.cpp \
# APIs
    $${PWD}/OAIOrdersApi.cpp \
    $${PWD}/OAISessionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
