QT += network

HEADERS += \
# Models
    $${PWD}/OAIAspectRecommendations.h \
    $${PWD}/OAIComplianceDetail.h \
    $${PWD}/OAIComplianceSummary.h \
    $${PWD}/OAIComplianceSummaryInfo.h \
    $${PWD}/OAIComplianceViolation.h \
    $${PWD}/OAICorrectiveRecommendations.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAINameValueList.h \
    $${PWD}/OAIPagedComplianceViolationCollection.h \
    $${PWD}/OAIProductRecommendation.h \
    $${PWD}/OAISuppressViolationRequest.h \
    $${PWD}/OAIVariationDetails.h \
# APIs
    $${PWD}/OAIListingViolationApi.h \
    $${PWD}/OAIListingViolationSummaryApi.h \
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
    $${PWD}/OAIAspectRecommendations.cpp \
    $${PWD}/OAIComplianceDetail.cpp \
    $${PWD}/OAIComplianceSummary.cpp \
    $${PWD}/OAIComplianceSummaryInfo.cpp \
    $${PWD}/OAIComplianceViolation.cpp \
    $${PWD}/OAICorrectiveRecommendations.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAINameValueList.cpp \
    $${PWD}/OAIPagedComplianceViolationCollection.cpp \
    $${PWD}/OAIProductRecommendation.cpp \
    $${PWD}/OAISuppressViolationRequest.cpp \
    $${PWD}/OAIVariationDetails.cpp \
# APIs
    $${PWD}/OAIListingViolationApi.cpp \
    $${PWD}/OAIListingViolationSummaryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
