QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdministrationRegion.h \
    $${PWD}/OAIAdministrativeBody.h \
    $${PWD}/OAICandidate.h \
    $${PWD}/OAIChannel.h \
    $${PWD}/OAIContest.h \
    $${PWD}/OAIDivisionSearchResponse.h \
    $${PWD}/OAIDivisionSearchResult.h \
    $${PWD}/OAIElection.h \
    $${PWD}/OAIElectionOfficial.h \
    $${PWD}/OAIElectionsQueryResponse.h \
    $${PWD}/OAIElectoralDistrict.h \
    $${PWD}/OAIGeographicDivision.h \
    $${PWD}/OAIOffice.h \
    $${PWD}/OAIOfficial.h \
    $${PWD}/OAIPollingLocation.h \
    $${PWD}/OAIPrecinct.h \
    $${PWD}/OAIRepresentativeInfoData.h \
    $${PWD}/OAIRepresentativeInfoResponse.h \
    $${PWD}/OAISimpleAddressType.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAIVoterInfoResponse.h \
# APIs
    $${PWD}/OAIDivisionsApi.h \
    $${PWD}/OAIElectionsApi.h \
    $${PWD}/OAIRepresentativesApi.h \
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
    $${PWD}/OAIAdministrationRegion.cpp \
    $${PWD}/OAIAdministrativeBody.cpp \
    $${PWD}/OAICandidate.cpp \
    $${PWD}/OAIChannel.cpp \
    $${PWD}/OAIContest.cpp \
    $${PWD}/OAIDivisionSearchResponse.cpp \
    $${PWD}/OAIDivisionSearchResult.cpp \
    $${PWD}/OAIElection.cpp \
    $${PWD}/OAIElectionOfficial.cpp \
    $${PWD}/OAIElectionsQueryResponse.cpp \
    $${PWD}/OAIElectoralDistrict.cpp \
    $${PWD}/OAIGeographicDivision.cpp \
    $${PWD}/OAIOffice.cpp \
    $${PWD}/OAIOfficial.cpp \
    $${PWD}/OAIPollingLocation.cpp \
    $${PWD}/OAIPrecinct.cpp \
    $${PWD}/OAIRepresentativeInfoData.cpp \
    $${PWD}/OAIRepresentativeInfoResponse.cpp \
    $${PWD}/OAISimpleAddressType.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAIVoterInfoResponse.cpp \
# APIs
    $${PWD}/OAIDivisionsApi.cpp \
    $${PWD}/OAIElectionsApi.cpp \
    $${PWD}/OAIRepresentativesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
