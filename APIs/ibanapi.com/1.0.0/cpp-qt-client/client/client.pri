QT += network

HEADERS += \
# Models
    $${PWD}/OAI400.h \
    $${PWD}/OAI401.h \
    $${PWD}/OAI403.h \
    $${PWD}/OAI422.h \
    $${PWD}/OAIBalanceResponse.h \
    $${PWD}/OAIIBANResult.h \
    $${PWD}/OAIIBANResultBasic.h \
# APIs
    $${PWD}/OAIIBANAPIApi.h \
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
    $${PWD}/OAI400.cpp \
    $${PWD}/OAI401.cpp \
    $${PWD}/OAI403.cpp \
    $${PWD}/OAI422.cpp \
    $${PWD}/OAIBalanceResponse.cpp \
    $${PWD}/OAIIBANResult.cpp \
    $${PWD}/OAIIBANResultBasic.cpp \
# APIs
    $${PWD}/OAIIBANAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
