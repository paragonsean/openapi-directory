QT += network

HEADERS += \
# Models
    $${PWD}/OAIChallenge.h \
    $${PWD}/OAISignedData.h \
    $${PWD}/OAIVerifyChallengeResponseRequest.h \
    $${PWD}/OAIVerifyChallengeResponseResult.h \
# APIs
    $${PWD}/OAIChallengeApi.h \
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
    $${PWD}/OAIChallenge.cpp \
    $${PWD}/OAISignedData.cpp \
    $${PWD}/OAIVerifyChallengeResponseRequest.cpp \
    $${PWD}/OAIVerifyChallengeResponseResult.cpp \
# APIs
    $${PWD}/OAIChallengeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
