QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdaptiveApplicationControls_List_default_response.h \
    $${PWD}/OAIAdaptiveApplicationControls_List_default_response_error.h \
    $${PWD}/OAIAppWhitelistingGroup.h \
    $${PWD}/OAIAppWhitelistingGroupData.h \
    $${PWD}/OAIAppWhitelistingGroups.h \
    $${PWD}/OAIAppWhitelistingIssue.h \
    $${PWD}/OAIAppWhitelistingIssueSummary.h \
    $${PWD}/OAIAppWhitelistingPutGroupData.h \
    $${PWD}/OAIConfigurationStatus.h \
    $${PWD}/OAIEnforcementMode.h \
    $${PWD}/OAIFileType.h \
    $${PWD}/OAIPathRecommendation.h \
    $${PWD}/OAIProtectionMode.h \
    $${PWD}/OAIPublisherInfo.h \
    $${PWD}/OAIRecommendationAction.h \
    $${PWD}/OAIRecommendationStatus.h \
    $${PWD}/OAIRecommendationType.h \
    $${PWD}/OAISourceSystem.h \
    $${PWD}/OAIUserRecommendation.h \
    $${PWD}/OAIVmRecommendation.h \
# APIs
    $${PWD}/OAIApplicationWhitelistingsApi.h \
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
    $${PWD}/OAIAdaptiveApplicationControls_List_default_response.cpp \
    $${PWD}/OAIAdaptiveApplicationControls_List_default_response_error.cpp \
    $${PWD}/OAIAppWhitelistingGroup.cpp \
    $${PWD}/OAIAppWhitelistingGroupData.cpp \
    $${PWD}/OAIAppWhitelistingGroups.cpp \
    $${PWD}/OAIAppWhitelistingIssue.cpp \
    $${PWD}/OAIAppWhitelistingIssueSummary.cpp \
    $${PWD}/OAIAppWhitelistingPutGroupData.cpp \
    $${PWD}/OAIConfigurationStatus.cpp \
    $${PWD}/OAIEnforcementMode.cpp \
    $${PWD}/OAIFileType.cpp \
    $${PWD}/OAIPathRecommendation.cpp \
    $${PWD}/OAIProtectionMode.cpp \
    $${PWD}/OAIPublisherInfo.cpp \
    $${PWD}/OAIRecommendationAction.cpp \
    $${PWD}/OAIRecommendationStatus.cpp \
    $${PWD}/OAIRecommendationType.cpp \
    $${PWD}/OAISourceSystem.cpp \
    $${PWD}/OAIUserRecommendation.cpp \
    $${PWD}/OAIVmRecommendation.cpp \
# APIs
    $${PWD}/OAIApplicationWhitelistingsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
