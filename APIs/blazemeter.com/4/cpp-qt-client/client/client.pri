QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponse.h \
    $${PWD}/OAIUserModel1.h \
    $${PWD}/OAIUserModel2.h \
    $${PWD}/OAIUserModel3.h \
    $${PWD}/OAIUserModel4.h \
    $${PWD}/OAIUserModel5.h \
# APIs
    $${PWD}/OAIUserApi.h \
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
    $${PWD}/OAIApiResponse.cpp \
    $${PWD}/OAIUserModel1.cpp \
    $${PWD}/OAIUserModel2.cpp \
    $${PWD}/OAIUserModel3.cpp \
    $${PWD}/OAIUserModel4.cpp \
    $${PWD}/OAIUserModel5.cpp \
# APIs
    $${PWD}/OAIUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
