QT += network

HEADERS += \
# Models
    $${PWD}/OAIBehavioralEventHttpCompletionRequest.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
# APIs
    $${PWD}/OAICustomEventDataApi.h \
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
    $${PWD}/OAIBehavioralEventHttpCompletionRequest.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
# APIs
    $${PWD}/OAICustomEventDataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
