QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIContactDetail.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_cause.h \
    $${PWD}/OAIError_tracking.h \
    $${PWD}/OAIEventOccurenceDetail.h \
    $${PWD}/OAIEventsQuery.h \
    $${PWD}/OAIEventsSearchResponse.h \
    $${PWD}/OAIFeatureReference.h \
    $${PWD}/OAIGeoPt.h \
    $${PWD}/OAIImageMeta.h \
    $${PWD}/OAIOccurrenceReference.h \
    $${PWD}/OAIPlaceDetail.h \
    $${PWD}/OAIPlaceReference.h \
    $${PWD}/OAIPlacesQuery.h \
    $${PWD}/OAIPlacesSearchResponse.h \
    $${PWD}/OAISearchStatsMetaResult.h \
    $${PWD}/OAITicketOffer.h \
    $${PWD}/OAITicketOffer_inventory.h \
    $${PWD}/OAITimeframe.h \
    $${PWD}/OAIVirtualLocation.h \
# APIs
    $${PWD}/OAIEventsApi.h \
    $${PWD}/OAIPlacesApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIContactDetail.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_cause.cpp \
    $${PWD}/OAIError_tracking.cpp \
    $${PWD}/OAIEventOccurenceDetail.cpp \
    $${PWD}/OAIEventsQuery.cpp \
    $${PWD}/OAIEventsSearchResponse.cpp \
    $${PWD}/OAIFeatureReference.cpp \
    $${PWD}/OAIGeoPt.cpp \
    $${PWD}/OAIImageMeta.cpp \
    $${PWD}/OAIOccurrenceReference.cpp \
    $${PWD}/OAIPlaceDetail.cpp \
    $${PWD}/OAIPlaceReference.cpp \
    $${PWD}/OAIPlacesQuery.cpp \
    $${PWD}/OAIPlacesSearchResponse.cpp \
    $${PWD}/OAISearchStatsMetaResult.cpp \
    $${PWD}/OAITicketOffer.cpp \
    $${PWD}/OAITicketOffer_inventory.cpp \
    $${PWD}/OAITimeframe.cpp \
    $${PWD}/OAIVirtualLocation.cpp \
# APIs
    $${PWD}/OAIEventsApi.cpp \
    $${PWD}/OAIPlacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
