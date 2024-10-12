QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvisor.h \
    $${PWD}/OAIAdvisorsResultList.h \
    $${PWD}/OAIRecommendationAction.h \
    $${PWD}/OAIRecommendationActionProperties.h \
    $${PWD}/OAIRecommendationActionsResultList.h \
    $${PWD}/OAIRecommendedActionSessionsOperationStatus.h \
# APIs
    $${PWD}/OAIAdvisorsApi.h \
    $${PWD}/OAILocationBasedRecommendedActionSessionsOperationStatusApi.h \
    $${PWD}/OAILocationBasedRecommendedActionSessionsResultApi.h \
    $${PWD}/OAIRecommendedActionSessionsApi.h \
    $${PWD}/OAIRecommendedActionsApi.h \
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
    $${PWD}/OAIAdvisor.cpp \
    $${PWD}/OAIAdvisorsResultList.cpp \
    $${PWD}/OAIRecommendationAction.cpp \
    $${PWD}/OAIRecommendationActionProperties.cpp \
    $${PWD}/OAIRecommendationActionsResultList.cpp \
    $${PWD}/OAIRecommendedActionSessionsOperationStatus.cpp \
# APIs
    $${PWD}/OAIAdvisorsApi.cpp \
    $${PWD}/OAILocationBasedRecommendedActionSessionsOperationStatusApi.cpp \
    $${PWD}/OAILocationBasedRecommendedActionSessionsResultApi.cpp \
    $${PWD}/OAIRecommendedActionSessionsApi.cpp \
    $${PWD}/OAIRecommendedActionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
