QT += network

HEADERS += \
# Models
    $${PWD}/OAIBarcode.h \
    $${PWD}/OAIIssuingCountry.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIVerifyChecksum.h \
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
    $${PWD}/OAIBarcode.cpp \
    $${PWD}/OAIIssuingCountry.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIVerifyChecksum.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
