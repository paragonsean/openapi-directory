QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperationDisplayInfo.h \
    $${PWD}/OAIOperationEntity.h \
    $${PWD}/OAIOperationEntityListResult.h \
    $${PWD}/OAIRecommendationProperties.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIResourceRecommendationBase.h \
    $${PWD}/OAIResourceRecommendationBaseListResult.h \
    $${PWD}/OAIShortDescription.h \
    $${PWD}/OAISuppressionContract.h \
# APIs
    $${PWD}/OAIGenerateRecommendationsApi.h \
    $${PWD}/OAIGetRecommendationsApi.h \
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAISuppressionsApi.h \
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
    $${PWD}/OAIOperationDisplayInfo.cpp \
    $${PWD}/OAIOperationEntity.cpp \
    $${PWD}/OAIOperationEntityListResult.cpp \
    $${PWD}/OAIRecommendationProperties.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIResourceRecommendationBase.cpp \
    $${PWD}/OAIResourceRecommendationBaseListResult.cpp \
    $${PWD}/OAIShortDescription.cpp \
    $${PWD}/OAISuppressionContract.cpp \
# APIs
    $${PWD}/OAIGenerateRecommendationsApi.cpp \
    $${PWD}/OAIGetRecommendationsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAISuppressionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
