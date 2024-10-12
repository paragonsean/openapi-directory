QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleSearchIdeahubV1betaAvailableLocale.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdea.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdeaActivity.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdeaState.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaListAvailableLocalesResponse.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaListIdeasResponse.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaTopic.h \
    $${PWD}/OAIGoogleSearchIdeahubV1betaTopicState.h \
# APIs
    $${PWD}/OAIPlatformsApi.h \
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
    $${PWD}/OAIGoogleSearchIdeahubV1betaAvailableLocale.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdea.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdeaActivity.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaIdeaState.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaListAvailableLocalesResponse.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaListIdeasResponse.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaTopic.cpp \
    $${PWD}/OAIGoogleSearchIdeahubV1betaTopicState.cpp \
# APIs
    $${PWD}/OAIPlatformsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
