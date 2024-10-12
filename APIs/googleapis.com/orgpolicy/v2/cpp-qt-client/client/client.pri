QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleCloudOrgpolicyV2AlternatePolicySpec.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2Constraint.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ConstraintListConstraint.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2CustomConstraint.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListConstraintsResponse.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListCustomConstraintsResponse.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListPoliciesResponse.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2Policy.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpec.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpecPolicyRule.h \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues.h \
    $${PWD}/OAIGoogleTypeExpr.h \
# APIs
    $${PWD}/OAIOrganizationsApi.h \
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIGoogleCloudOrgpolicyV2AlternatePolicySpec.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2Constraint.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ConstraintListConstraint.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2CustomConstraint.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListConstraintsResponse.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListCustomConstraintsResponse.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2ListPoliciesResponse.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2Policy.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpec.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpecPolicyRule.cpp \
    $${PWD}/OAIGoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues.cpp \
    $${PWD}/OAIGoogleTypeExpr.cpp \
# APIs
    $${PWD}/OAIOrganizationsApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
