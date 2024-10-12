QT += network

HEADERS += \
# Models
    $${PWD}/OAIDivisionGroupedByParty.h \
    $${PWD}/OAIMemberSearchQueryParameters.h \
    $${PWD}/OAIMemberVotingRecord.h \
    $${PWD}/OAIPartyVoteResult.h \
    $${PWD}/OAIPublishedDivision.h \
    $${PWD}/OAIQueryParameters.h \
    $${PWD}/OAIRecordedMember.h \
    $${PWD}/OAISearchQueryParameters.h \
# APIs
    $${PWD}/OAIDivisionsApi.h \
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
    $${PWD}/OAIDivisionGroupedByParty.cpp \
    $${PWD}/OAIMemberSearchQueryParameters.cpp \
    $${PWD}/OAIMemberVotingRecord.cpp \
    $${PWD}/OAIPartyVoteResult.cpp \
    $${PWD}/OAIPublishedDivision.cpp \
    $${PWD}/OAIQueryParameters.cpp \
    $${PWD}/OAIRecordedMember.cpp \
    $${PWD}/OAISearchQueryParameters.cpp \
# APIs
    $${PWD}/OAIDivisionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
