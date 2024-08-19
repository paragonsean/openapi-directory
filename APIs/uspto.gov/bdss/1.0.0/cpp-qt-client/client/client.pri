QT += network

HEADERS += \
# Models
    $${PWD}/OAIProductFileModel.h \
    $${PWD}/OAIProductModel.h \
    $${PWD}/OAIProductModelShort.h \
# APIs
    $${PWD}/OAIProductsApi.h \
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
    $${PWD}/OAIProductFileModel.cpp \
    $${PWD}/OAIProductModel.cpp \
    $${PWD}/OAIProductModelShort.cpp \
# APIs
    $${PWD}/OAIProductsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
