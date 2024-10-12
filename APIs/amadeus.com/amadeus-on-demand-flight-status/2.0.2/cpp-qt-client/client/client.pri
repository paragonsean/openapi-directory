QT += network

HEADERS += \
# Models
    $${PWD}/OAIAircraftEquipment.h \
    $${PWD}/OAIArrival.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIDatedFlight.h \
    $${PWD}/OAIDelay.h \
    $${PWD}/OAIDeparture.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_401.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIFlightDesignator.h \
    $${PWD}/OAIFlightPoint.h \
    $${PWD}/OAIGate.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILeg.h \
    $${PWD}/OAIPartnership.h \
    $${PWD}/OAISegment.h \
    $${PWD}/OAISuccess_Flights_.h \
    $${PWD}/OAITerminal.h \
    $${PWD}/OAITiming.h \
# APIs
    $${PWD}/OAIFlightsApi.h \
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
    $${PWD}/OAIAircraftEquipment.cpp \
    $${PWD}/OAIArrival.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIDatedFlight.cpp \
    $${PWD}/OAIDelay.cpp \
    $${PWD}/OAIDeparture.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_401.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIFlightDesignator.cpp \
    $${PWD}/OAIFlightPoint.cpp \
    $${PWD}/OAIGate.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILeg.cpp \
    $${PWD}/OAIPartnership.cpp \
    $${PWD}/OAISegment.cpp \
    $${PWD}/OAISuccess_Flights_.cpp \
    $${PWD}/OAITerminal.cpp \
    $${PWD}/OAITiming.cpp \
# APIs
    $${PWD}/OAIFlightsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
