QT += network

HEADERS += \
# Models
    $${PWD}/OAIBreadcrumbs_API_Models_Address_AddressResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_AddressRiskResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_ExposureResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_RiskExposureResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Node_NodeRequest.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Node_NodeResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Pathfinder_PathfinderRequest.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Pathfinder_PathfinderResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Sanction_SanctionedRequest.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Sanction_SanctionedResponse.h \
    $${PWD}/OAIBreadcrumbs_API_Models_Transaction_RiskResponse.h \
    $${PWD}/OAIBreadcrumbs_Response_UnauthorizedResponse.h \
    $${PWD}/OAIBreadcrumbs_Response_UnprocessableResponse.h \
# APIs
    $${PWD}/OAINodeApi.h \
    $${PWD}/OAIPathfinderApi.h \
    $${PWD}/OAIRiskApi.h \
    $${PWD}/OAISanctionApi.h \
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
    $${PWD}/OAIBreadcrumbs_API_Models_Address_AddressResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_AddressRiskResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_ExposureResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Address_RiskExposureResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Node_NodeRequest.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Node_NodeResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Pathfinder_PathfinderRequest.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Pathfinder_PathfinderResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Sanction_SanctionedRequest.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Sanction_SanctionedResponse.cpp \
    $${PWD}/OAIBreadcrumbs_API_Models_Transaction_RiskResponse.cpp \
    $${PWD}/OAIBreadcrumbs_Response_UnauthorizedResponse.cpp \
    $${PWD}/OAIBreadcrumbs_Response_UnprocessableResponse.cpp \
# APIs
    $${PWD}/OAINodeApi.cpp \
    $${PWD}/OAIPathfinderApi.cpp \
    $${PWD}/OAIRiskApi.cpp \
    $${PWD}/OAISanctionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
