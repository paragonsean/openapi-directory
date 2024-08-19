QT += network

HEADERS += \
# Models
    $${PWD}/OAIAction.h \
    $${PWD}/OAIAnswer.h \
    $${PWD}/OAICreativeWork.h \
    $${PWD}/OAIEntitiesEntityPresentationInfo.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIGeoCoordinates.h \
    $${PWD}/OAIIdentifiable.h \
    $${PWD}/OAIIntangible.h \
    $${PWD}/OAIPlace.h \
    $${PWD}/OAIPlaces.h \
    $${PWD}/OAIPostalAddress.h \
    $${PWD}/OAIQueryContext.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIResponseBase.h \
    $${PWD}/OAISearchAction.h \
    $${PWD}/OAISearchResponse.h \
    $${PWD}/OAISearchResultsAnswer.h \
    $${PWD}/OAIStructuredValue.h \
    $${PWD}/OAIThing.h \
# APIs
    $${PWD}/OAILocalSearchApi.h \
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
    $${PWD}/OAIAction.cpp \
    $${PWD}/OAIAnswer.cpp \
    $${PWD}/OAICreativeWork.cpp \
    $${PWD}/OAIEntitiesEntityPresentationInfo.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIGeoCoordinates.cpp \
    $${PWD}/OAIIdentifiable.cpp \
    $${PWD}/OAIIntangible.cpp \
    $${PWD}/OAIPlace.cpp \
    $${PWD}/OAIPlaces.cpp \
    $${PWD}/OAIPostalAddress.cpp \
    $${PWD}/OAIQueryContext.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIResponseBase.cpp \
    $${PWD}/OAISearchAction.cpp \
    $${PWD}/OAISearchResponse.cpp \
    $${PWD}/OAISearchResultsAnswer.cpp \
    $${PWD}/OAIStructuredValue.cpp \
    $${PWD}/OAIThing.cpp \
# APIs
    $${PWD}/OAILocalSearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
