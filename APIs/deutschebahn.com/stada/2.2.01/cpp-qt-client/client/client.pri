QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAufgabentraeger.h \
    $${PWD}/OAIEVANumber.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIGeographicPoint.h \
    $${PWD}/OAIOpeningHours.h \
    $${PWD}/OAIPartial.h \
    $${PWD}/OAIRegionalBereichRef.h \
    $${PWD}/OAIRegionalbereich.h \
    $${PWD}/OAIRiL100Identifier.h \
    $${PWD}/OAISZentrale.h \
    $${PWD}/OAISZentraleQuery.h \
    $${PWD}/OAISZentraleRef.h \
    $${PWD}/OAISchedule.h \
    $${PWD}/OAIStation.h \
    $${PWD}/OAIStationManagement.h \
    $${PWD}/OAIStationManagementRef.h \
    $${PWD}/OAIStationQuery.h \
    $${PWD}/OAITimetableOffice.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAufgabentraeger.cpp \
    $${PWD}/OAIEVANumber.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIGeographicPoint.cpp \
    $${PWD}/OAIOpeningHours.cpp \
    $${PWD}/OAIPartial.cpp \
    $${PWD}/OAIRegionalBereichRef.cpp \
    $${PWD}/OAIRegionalbereich.cpp \
    $${PWD}/OAIRiL100Identifier.cpp \
    $${PWD}/OAISZentrale.cpp \
    $${PWD}/OAISZentraleQuery.cpp \
    $${PWD}/OAISZentraleRef.cpp \
    $${PWD}/OAISchedule.cpp \
    $${PWD}/OAIStation.cpp \
    $${PWD}/OAIStationManagement.cpp \
    $${PWD}/OAIStationManagementRef.cpp \
    $${PWD}/OAIStationQuery.cpp \
    $${PWD}/OAITimetableOffice.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
