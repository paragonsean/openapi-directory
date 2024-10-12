QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta_Link.h \
    $${PWD}/OAIDelay_Prediction.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAIPrediction.h \
    $${PWD}/OAIPredictionResultType.h \
# APIs
    $${PWD}/OAIFlightDelayPredictionApi.h \
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
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta_Link.cpp \
    $${PWD}/OAIDelay_Prediction.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAIPrediction.cpp \
    $${PWD}/OAIPredictionResultType.cpp \
# APIs
    $${PWD}/OAIFlightDelayPredictionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
