QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorization.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIErrorResponse_error.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIPlan.h \
    $${PWD}/OAIRegistrationAssignment.h \
    $${PWD}/OAIRegistrationAssignmentList.h \
    $${PWD}/OAIRegistrationAssignmentProperties.h \
    $${PWD}/OAIRegistrationAssignmentProperties_registrationDefinition.h \
    $${PWD}/OAIRegistrationAssignmentProperties_registrationDefinition_properties.h \
    $${PWD}/OAIRegistrationDefinition.h \
    $${PWD}/OAIRegistrationDefinitionList.h \
    $${PWD}/OAIRegistrationDefinitionProperties.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIRegistrationAssignmentsApi.h \
    $${PWD}/OAIRegistrationDefinitionsApi.h \
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
    $${PWD}/OAIAuthorization.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIErrorResponse_error.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIPlan.cpp \
    $${PWD}/OAIRegistrationAssignment.cpp \
    $${PWD}/OAIRegistrationAssignmentList.cpp \
    $${PWD}/OAIRegistrationAssignmentProperties.cpp \
    $${PWD}/OAIRegistrationAssignmentProperties_registrationDefinition.cpp \
    $${PWD}/OAIRegistrationAssignmentProperties_registrationDefinition_properties.cpp \
    $${PWD}/OAIRegistrationDefinition.cpp \
    $${PWD}/OAIRegistrationDefinitionList.cpp \
    $${PWD}/OAIRegistrationDefinitionProperties.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIRegistrationAssignmentsApi.cpp \
    $${PWD}/OAIRegistrationDefinitionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
