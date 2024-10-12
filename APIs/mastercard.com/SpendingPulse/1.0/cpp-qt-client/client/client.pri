QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorSchema.h \
    $${PWD}/OAIErrors.h \
    $${PWD}/OAIGasWeeklyArray.h \
    $${PWD}/OAIGasWeeklyList.h \
    $${PWD}/OAIGasWeeklyListResponse.h \
    $${PWD}/OAIGasWeeklyRecord.h \
    $${PWD}/OAIParameter.h \
    $${PWD}/OAIParameterArray.h \
    $${PWD}/OAIParameterList.h \
    $${PWD}/OAIParameterListResponse.h \
    $${PWD}/OAISpendingPulseArray.h \
    $${PWD}/OAISpendingPulseList.h \
    $${PWD}/OAISpendingPulseListResponse.h \
    $${PWD}/OAISpendingPulseRecord.h \
    $${PWD}/OAISubscription.h \
    $${PWD}/OAISubscriptionArray.h \
    $${PWD}/OAISubscriptionList.h \
    $${PWD}/OAISubscriptionListResponse.h \
# APIs
    $${PWD}/OAIGasWeeklyApi.h \
    $${PWD}/OAIParametersApi.h \
    $${PWD}/OAISpendingPulseReportApi.h \
    $${PWD}/OAISubscriptionApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorSchema.cpp \
    $${PWD}/OAIErrors.cpp \
    $${PWD}/OAIGasWeeklyArray.cpp \
    $${PWD}/OAIGasWeeklyList.cpp \
    $${PWD}/OAIGasWeeklyListResponse.cpp \
    $${PWD}/OAIGasWeeklyRecord.cpp \
    $${PWD}/OAIParameter.cpp \
    $${PWD}/OAIParameterArray.cpp \
    $${PWD}/OAIParameterList.cpp \
    $${PWD}/OAIParameterListResponse.cpp \
    $${PWD}/OAISpendingPulseArray.cpp \
    $${PWD}/OAISpendingPulseList.cpp \
    $${PWD}/OAISpendingPulseListResponse.cpp \
    $${PWD}/OAISpendingPulseRecord.cpp \
    $${PWD}/OAISubscription.cpp \
    $${PWD}/OAISubscriptionArray.cpp \
    $${PWD}/OAISubscriptionList.cpp \
    $${PWD}/OAISubscriptionListResponse.cpp \
# APIs
    $${PWD}/OAIGasWeeklyApi.cpp \
    $${PWD}/OAIParametersApi.cpp \
    $${PWD}/OAISpendingPulseReportApi.cpp \
    $${PWD}/OAISubscriptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
