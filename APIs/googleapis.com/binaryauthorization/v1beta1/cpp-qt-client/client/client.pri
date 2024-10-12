QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdmissionRule.h \
    $${PWD}/OAIAdmissionWhitelistPattern.h \
    $${PWD}/OAIAttestationOccurrence.h \
    $${PWD}/OAIAttestor.h \
    $${PWD}/OAIAttestorPublicKey.h \
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIIamPolicy.h \
    $${PWD}/OAIJwt.h \
    $${PWD}/OAIListAttestorsResponse.h \
    $${PWD}/OAIPkixPublicKey.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAISignature.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAIUserOwnedDrydockNote.h \
    $${PWD}/OAIValidateAttestationOccurrenceRequest.h \
    $${PWD}/OAIValidateAttestationOccurrenceResponse.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
    $${PWD}/OAISystempolicyApi.h \
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
    $${PWD}/OAIAdmissionRule.cpp \
    $${PWD}/OAIAdmissionWhitelistPattern.cpp \
    $${PWD}/OAIAttestationOccurrence.cpp \
    $${PWD}/OAIAttestor.cpp \
    $${PWD}/OAIAttestorPublicKey.cpp \
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIIamPolicy.cpp \
    $${PWD}/OAIJwt.cpp \
    $${PWD}/OAIListAttestorsResponse.cpp \
    $${PWD}/OAIPkixPublicKey.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAISignature.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAIUserOwnedDrydockNote.cpp \
    $${PWD}/OAIValidateAttestationOccurrenceRequest.cpp \
    $${PWD}/OAIValidateAttestationOccurrenceResponse.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAISystempolicyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
