QT += network

HEADERS += \
# Models
    $${PWD}/OAIBadRequest.h \
    $${PWD}/OAICompanyBoardMembersMulti.h \
    $${PWD}/OAICompanyBoardMembersResult.h \
    $${PWD}/OAICompanyBoardMembersResult_boardMembers_inner.h \
    $${PWD}/OAICompanyCreditDecisionResult.h \
    $${PWD}/OAICompanyEconomyOverviewMulti.h \
    $${PWD}/OAICompanyEconomyOverviewResult.h \
    $${PWD}/OAICompanyEventRequestBody.h \
    $${PWD}/OAICompanyEventRequestBody_requests_inner.h \
    $${PWD}/OAICompanyEventResult.h \
    $${PWD}/OAICompanyEventResult_responses_inner.h \
    $${PWD}/OAICompanyLookupRequestBody.h \
    $${PWD}/OAICompanyOverviewMulti.h \
    $${PWD}/OAICompanyOverviewResult.h \
    $${PWD}/OAICompanyRejection.h \
    $${PWD}/OAICompanySignatoryMulti.h \
    $${PWD}/OAICompanySignatoryResult.h \
    $${PWD}/OAINotFound.h \
    $${PWD}/OAIResponseInfo.h \
    $${PWD}/OAIServerError.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIBadRequest.cpp \
    $${PWD}/OAICompanyBoardMembersMulti.cpp \
    $${PWD}/OAICompanyBoardMembersResult.cpp \
    $${PWD}/OAICompanyBoardMembersResult_boardMembers_inner.cpp \
    $${PWD}/OAICompanyCreditDecisionResult.cpp \
    $${PWD}/OAICompanyEconomyOverviewMulti.cpp \
    $${PWD}/OAICompanyEconomyOverviewResult.cpp \
    $${PWD}/OAICompanyEventRequestBody.cpp \
    $${PWD}/OAICompanyEventRequestBody_requests_inner.cpp \
    $${PWD}/OAICompanyEventResult.cpp \
    $${PWD}/OAICompanyEventResult_responses_inner.cpp \
    $${PWD}/OAICompanyLookupRequestBody.cpp \
    $${PWD}/OAICompanyOverviewMulti.cpp \
    $${PWD}/OAICompanyOverviewResult.cpp \
    $${PWD}/OAICompanyRejection.cpp \
    $${PWD}/OAICompanySignatoryMulti.cpp \
    $${PWD}/OAICompanySignatoryResult.cpp \
    $${PWD}/OAINotFound.cpp \
    $${PWD}/OAIResponseInfo.cpp \
    $${PWD}/OAIServerError.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
