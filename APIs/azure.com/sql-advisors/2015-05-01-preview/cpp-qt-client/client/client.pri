QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvisor.h \
    $${PWD}/OAIAdvisorProperties.h \
    $${PWD}/OAIRecommendedAction.h \
    $${PWD}/OAIRecommendedActionErrorInfo.h \
    $${PWD}/OAIRecommendedActionImpactRecord.h \
    $${PWD}/OAIRecommendedActionImplementationInfo.h \
    $${PWD}/OAIRecommendedActionMetricInfo.h \
    $${PWD}/OAIRecommendedActionProperties.h \
    $${PWD}/OAIRecommendedActionStateInfo.h \
# APIs
    $${PWD}/OAIDatabaseAdvisorsApi.h \
    $${PWD}/OAIDatabaseRecommendedActionsApi.h \
    $${PWD}/OAIServerAdvisorsApi.h \
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
    $${PWD}/OAIAdvisorProperties.cpp \
    $${PWD}/OAIRecommendedAction.cpp \
    $${PWD}/OAIRecommendedActionErrorInfo.cpp \
    $${PWD}/OAIRecommendedActionImpactRecord.cpp \
    $${PWD}/OAIRecommendedActionImplementationInfo.cpp \
    $${PWD}/OAIRecommendedActionMetricInfo.cpp \
    $${PWD}/OAIRecommendedActionProperties.cpp \
    $${PWD}/OAIRecommendedActionStateInfo.cpp \
# APIs
    $${PWD}/OAIDatabaseAdvisorsApi.cpp \
    $${PWD}/OAIDatabaseRecommendedActionsApi.cpp \
    $${PWD}/OAIServerAdvisorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
