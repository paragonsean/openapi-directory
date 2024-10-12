QT += network

HEADERS += \
# Models
    $${PWD}/OAIComparators.h \
    $${PWD}/OAIDivisionGroupByPartyViewModel.h \
    $${PWD}/OAIDivisionViewModel.h \
    $${PWD}/OAIMemberViewModel.h \
    $${PWD}/OAIMemberVotingRecordViewModel.h \
    $${PWD}/OAIPartyVoteResultViewModel.h \
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
    $${PWD}/OAIComparators.cpp \
    $${PWD}/OAIDivisionGroupByPartyViewModel.cpp \
    $${PWD}/OAIDivisionViewModel.cpp \
    $${PWD}/OAIMemberViewModel.cpp \
    $${PWD}/OAIMemberVotingRecordViewModel.cpp \
    $${PWD}/OAIPartyVoteResultViewModel.cpp \
# APIs
    $${PWD}/OAIDivisionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
