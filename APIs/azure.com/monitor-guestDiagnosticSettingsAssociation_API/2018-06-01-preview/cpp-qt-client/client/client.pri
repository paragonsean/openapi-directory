QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIGuestDiagnosticSettingsAssociation.h \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationList.h \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationResource.h \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationResourcePatch.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIGuestDiagnosticsSettingsAssociationApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIGuestDiagnosticSettingsAssociation.cpp \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationList.cpp \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationResource.cpp \
    $${PWD}/OAIGuestDiagnosticSettingsAssociationResourcePatch.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIGuestDiagnosticsSettingsAssociationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
