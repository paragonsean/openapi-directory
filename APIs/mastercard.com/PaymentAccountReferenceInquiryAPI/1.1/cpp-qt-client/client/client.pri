QT += network

HEADERS += \
# Models
    $${PWD}/OAIEncryptedPayloadData.h \
    $${PWD}/OAIEncryptedPayloadOut.h \
    $${PWD}/OAIGetPaymentAccountReferenceRequestSchema.h \
    $${PWD}/OAIGetPaymentAccountReferenceResponseSchema.h \
# APIs
    $${PWD}/OAIGetPaymentAccountReferenceApi.h \
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
    $${PWD}/OAIEncryptedPayloadData.cpp \
    $${PWD}/OAIEncryptedPayloadOut.cpp \
    $${PWD}/OAIGetPaymentAccountReferenceRequestSchema.cpp \
    $${PWD}/OAIGetPaymentAccountReferenceResponseSchema.cpp \
# APIs
    $${PWD}/OAIGetPaymentAccountReferenceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
