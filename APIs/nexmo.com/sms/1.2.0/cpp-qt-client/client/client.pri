QT += network

HEADERS += \
# Models
    $${PWD}/OAIDeliveryReceipt.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorMessage.h \
    $${PWD}/OAIErrorXml.h \
    $${PWD}/OAIInboundMessage.h \
    $${PWD}/OAIMessage.h \
    $${PWD}/OAISMS.h \
    $${PWD}/OAISMSXml.h \
    $${PWD}/OAISend_an_sms_200_response.h \
    $${PWD}/OAISend_an_sms_200_response_1.h \
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
    $${PWD}/OAIDeliveryReceipt.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorMessage.cpp \
    $${PWD}/OAIErrorXml.cpp \
    $${PWD}/OAIInboundMessage.cpp \
    $${PWD}/OAIMessage.cpp \
    $${PWD}/OAISMS.cpp \
    $${PWD}/OAISMSXml.cpp \
    $${PWD}/OAISend_an_sms_200_response.cpp \
    $${PWD}/OAISend_an_sms_200_response_1.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
