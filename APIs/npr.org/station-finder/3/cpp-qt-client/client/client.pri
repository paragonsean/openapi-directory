QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbstractCDocLink.h \
    $${PWD}/OAIAbstractLink.h \
    $${PWD}/OAIAffiliation.h \
    $${PWD}/OAICollectionDocument.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDocument.h \
    $${PWD}/OAIStationBrandData.h \
    $${PWD}/OAIStationBrandLink.h \
    $${PWD}/OAIStationData.h \
    $${PWD}/OAIStationDocument.h \
    $${PWD}/OAIStationDonationLink.h \
    $${PWD}/OAIStationEligibilityData.h \
    $${PWD}/OAIStationLink.h \
    $${PWD}/OAIStationLinks.h \
    $${PWD}/OAIStationListDocument.h \
    $${PWD}/OAIStationNetworkData.h \
    $${PWD}/OAIStationNetworkTierOneData.h \
    $${PWD}/OAIStationNetworkTierThreeData.h \
    $${PWD}/OAIStationNetworkTierTwoData.h \
    $${PWD}/OAIStationNewscastData.h \
    $${PWD}/OAIStationPodcastsLink.h \
    $${PWD}/OAIStationRelatedLink.h \
    $${PWD}/OAIStationSearchMetaData.h \
    $${PWD}/OAIStationStreamsLink.h \
# APIs
    $${PWD}/OAIStationfinderApi.h \
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
    $${PWD}/OAIAbstractCDocLink.cpp \
    $${PWD}/OAIAbstractLink.cpp \
    $${PWD}/OAIAffiliation.cpp \
    $${PWD}/OAICollectionDocument.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDocument.cpp \
    $${PWD}/OAIStationBrandData.cpp \
    $${PWD}/OAIStationBrandLink.cpp \
    $${PWD}/OAIStationData.cpp \
    $${PWD}/OAIStationDocument.cpp \
    $${PWD}/OAIStationDonationLink.cpp \
    $${PWD}/OAIStationEligibilityData.cpp \
    $${PWD}/OAIStationLink.cpp \
    $${PWD}/OAIStationLinks.cpp \
    $${PWD}/OAIStationListDocument.cpp \
    $${PWD}/OAIStationNetworkData.cpp \
    $${PWD}/OAIStationNetworkTierOneData.cpp \
    $${PWD}/OAIStationNetworkTierThreeData.cpp \
    $${PWD}/OAIStationNetworkTierTwoData.cpp \
    $${PWD}/OAIStationNewscastData.cpp \
    $${PWD}/OAIStationPodcastsLink.cpp \
    $${PWD}/OAIStationRelatedLink.cpp \
    $${PWD}/OAIStationSearchMetaData.cpp \
    $${PWD}/OAIStationStreamsLink.cpp \
# APIs
    $${PWD}/OAIStationfinderApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
