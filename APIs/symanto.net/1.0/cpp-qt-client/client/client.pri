QT += network

HEADERS += \
# Models
    $${PWD}/OAILanguageDetection.h \
    $${PWD}/OAILanguagePredicted.h \
    $${PWD}/OAIPost.h \
    $${PWD}/OAIPostPredicted.h \
    $${PWD}/OAIPrediction.h \
    $${PWD}/OAISentiment.h \
    $${PWD}/OAITopic.h \
    $${PWD}/OAITopicSentiment.h \
    $${PWD}/OAITopicSentimentOutput.h \
    $${PWD}/OAIValidationError.h \
    $${PWD}/OAIValidationErrors.h \
# APIs
    $${PWD}/OAITextAnalysisApi.h \
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
    $${PWD}/OAILanguageDetection.cpp \
    $${PWD}/OAILanguagePredicted.cpp \
    $${PWD}/OAIPost.cpp \
    $${PWD}/OAIPostPredicted.cpp \
    $${PWD}/OAIPrediction.cpp \
    $${PWD}/OAISentiment.cpp \
    $${PWD}/OAITopic.cpp \
    $${PWD}/OAITopicSentiment.cpp \
    $${PWD}/OAITopicSentimentOutput.cpp \
    $${PWD}/OAIValidationError.cpp \
    $${PWD}/OAIValidationErrors.cpp \
# APIs
    $${PWD}/OAITextAnalysisApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
