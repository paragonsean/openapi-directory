QT += network

HEADERS += \
# Models
    $${PWD}/OAIAppServiceCertificate.h \
    $${PWD}/OAIAppServiceCertificateCollection.h \
    $${PWD}/OAIAppServiceCertificateOrder.h \
    $${PWD}/OAIAppServiceCertificateOrderCollection.h \
    $${PWD}/OAIAppServiceCertificateOrderPatchResource.h \
    $${PWD}/OAIAppServiceCertificateOrders_ResendRequestEmails_request.h \
    $${PWD}/OAIAppServiceCertificatePatchResource.h \
    $${PWD}/OAIAppServiceCertificateResource.h \
    $${PWD}/OAICertificateDetails.h \
    $${PWD}/OAICertificateEmail.h \
    $${PWD}/OAICertificateOrderAction.h \
    $${PWD}/OAIReissueCertificateOrderRequest.h \
    $${PWD}/OAIRenewCertificateOrderRequest.h \
    $${PWD}/OAISiteSeal.h \
    $${PWD}/OAISiteSealRequest.h \
# APIs
    $${PWD}/OAIAppServiceCertificateOrdersApi.h \
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
    $${PWD}/OAIAppServiceCertificate.cpp \
    $${PWD}/OAIAppServiceCertificateCollection.cpp \
    $${PWD}/OAIAppServiceCertificateOrder.cpp \
    $${PWD}/OAIAppServiceCertificateOrderCollection.cpp \
    $${PWD}/OAIAppServiceCertificateOrderPatchResource.cpp \
    $${PWD}/OAIAppServiceCertificateOrders_ResendRequestEmails_request.cpp \
    $${PWD}/OAIAppServiceCertificatePatchResource.cpp \
    $${PWD}/OAIAppServiceCertificateResource.cpp \
    $${PWD}/OAICertificateDetails.cpp \
    $${PWD}/OAICertificateEmail.cpp \
    $${PWD}/OAICertificateOrderAction.cpp \
    $${PWD}/OAIReissueCertificateOrderRequest.cpp \
    $${PWD}/OAIRenewCertificateOrderRequest.cpp \
    $${PWD}/OAISiteSeal.cpp \
    $${PWD}/OAISiteSealRequest.cpp \
# APIs
    $${PWD}/OAIAppServiceCertificateOrdersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
