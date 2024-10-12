QT += network

HEADERS += \
# Models
    $${PWD}/OAIAxis.h \
    $${PWD}/OAIWebfont.h \
    $${PWD}/OAIWebfontList.h \
# APIs
    $${PWD}/OAIWebfontsApi.h \
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
    $${PWD}/OAIAxis.cpp \
    $${PWD}/OAIWebfont.cpp \
    $${PWD}/OAIWebfontList.cpp \
# APIs
    $${PWD}/OAIWebfontsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
