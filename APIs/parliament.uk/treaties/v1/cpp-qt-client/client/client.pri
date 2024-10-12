QT += network

HEADERS += \
# Models
    $${PWD}/OAIBusinessItem.h \
    $${PWD}/OAIBusinessItemHouse.h \
    $${PWD}/OAIBusinessItemResource.h \
    $${PWD}/OAIBusinessItemResourceCollection.h \
    $${PWD}/OAIDepartment.h \
    $${PWD}/OAIGovernmentOrganisation.h \
    $${PWD}/OAIGovernmentOrganisationResource.h \
    $${PWD}/OAIGovernmentOrganisationResourceCollection.h \
    $${PWD}/OAIHouse.h \
    $${PWD}/OAILink.h \
    $${PWD}/OAIParliamentaryConclusion.h \
    $${PWD}/OAIParliamentaryProcess.h \
    $${PWD}/OAISeriesMembership.h \
    $${PWD}/OAISeriesMembershipResource.h \
    $${PWD}/OAISeriesMembershipResourceCollection.h \
    $${PWD}/OAISeriesMembershipType.h \
    $${PWD}/OAITreaty.h \
    $${PWD}/OAITreatyResource.h \
    $${PWD}/OAITreatyResourceCollection.h \
    $${PWD}/OAITreatySeriesMembership.h \
# APIs
    $${PWD}/OAIBusinessItemApi.h \
    $${PWD}/OAIGovernmentOrganisationApi.h \
    $${PWD}/OAISeriesMembershipApi.h \
    $${PWD}/OAITreatyApi.h \
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
    $${PWD}/OAIBusinessItem.cpp \
    $${PWD}/OAIBusinessItemHouse.cpp \
    $${PWD}/OAIBusinessItemResource.cpp \
    $${PWD}/OAIBusinessItemResourceCollection.cpp \
    $${PWD}/OAIDepartment.cpp \
    $${PWD}/OAIGovernmentOrganisation.cpp \
    $${PWD}/OAIGovernmentOrganisationResource.cpp \
    $${PWD}/OAIGovernmentOrganisationResourceCollection.cpp \
    $${PWD}/OAIHouse.cpp \
    $${PWD}/OAILink.cpp \
    $${PWD}/OAIParliamentaryConclusion.cpp \
    $${PWD}/OAIParliamentaryProcess.cpp \
    $${PWD}/OAISeriesMembership.cpp \
    $${PWD}/OAISeriesMembershipResource.cpp \
    $${PWD}/OAISeriesMembershipResourceCollection.cpp \
    $${PWD}/OAISeriesMembershipType.cpp \
    $${PWD}/OAITreaty.cpp \
    $${PWD}/OAITreatyResource.cpp \
    $${PWD}/OAITreatyResourceCollection.cpp \
    $${PWD}/OAITreatySeriesMembership.cpp \
# APIs
    $${PWD}/OAIBusinessItemApi.cpp \
    $${PWD}/OAIGovernmentOrganisationApi.cpp \
    $${PWD}/OAISeriesMembershipApi.cpp \
    $${PWD}/OAITreatyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
