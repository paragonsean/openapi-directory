QT += network

HEADERS += \
# Models
    $${PWD}/OAIBatchInputSubscriptionBatchUpdateRequest.h \
    $${PWD}/OAIBatchResponseSubscriptionResponse.h \
    $${PWD}/OAIBatchResponseSubscriptionResponseWithErrors.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAISettingsChangeRequest.h \
    $${PWD}/OAISettingsResponse.h \
    $${PWD}/OAIStandardError.h \
    $${PWD}/OAISubscriptionBatchUpdateRequest.h \
    $${PWD}/OAISubscriptionCreateRequest.h \
    $${PWD}/OAISubscriptionListResponse.h \
    $${PWD}/OAISubscriptionPatchRequest.h \
    $${PWD}/OAISubscriptionResponse.h \
    $${PWD}/OAIThrottlingSettings.h \
# APIs
    $${PWD}/OAISettingsApi.h \
    $${PWD}/OAISubscriptionsApi.h \
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
    $${PWD}/OAIBatchInputSubscriptionBatchUpdateRequest.cpp \
    $${PWD}/OAIBatchResponseSubscriptionResponse.cpp \
    $${PWD}/OAIBatchResponseSubscriptionResponseWithErrors.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAISettingsChangeRequest.cpp \
    $${PWD}/OAISettingsResponse.cpp \
    $${PWD}/OAIStandardError.cpp \
    $${PWD}/OAISubscriptionBatchUpdateRequest.cpp \
    $${PWD}/OAISubscriptionCreateRequest.cpp \
    $${PWD}/OAISubscriptionListResponse.cpp \
    $${PWD}/OAISubscriptionPatchRequest.cpp \
    $${PWD}/OAISubscriptionResponse.cpp \
    $${PWD}/OAIThrottlingSettings.cpp \
# APIs
    $${PWD}/OAISettingsApi.cpp \
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
