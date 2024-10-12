QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIPageError.h \
# APIs
    $${PWD}/OAIAccountApi.h \
    $${PWD}/OAIHTMLApi.h \
    $${PWD}/OAISelectedHTMLApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIPageError.cpp \
# APIs
    $${PWD}/OAIAccountApi.cpp \
    $${PWD}/OAIHTMLApi.cpp \
    $${PWD}/OAISelectedHTMLApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
