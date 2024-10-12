QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcmeChallengeSet.h \
    $${PWD}/OAIAcmeTxtRecord.h \
    $${PWD}/OAIRotateChallengesRequest.h \
# APIs
    $${PWD}/OAIAcmeChallengeSetsApi.h \
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
    $${PWD}/OAIAcmeChallengeSet.cpp \
    $${PWD}/OAIAcmeTxtRecord.cpp \
    $${PWD}/OAIRotateChallengesRequest.cpp \
# APIs
    $${PWD}/OAIAcmeChallengeSetsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
