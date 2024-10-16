QT += network

HEADERS += \
# Models
    $${PWD}/OAIAutomaticInvitationVO.h \
    $${PWD}/OAIAutomaticInvitationsListVO.h \
    $${PWD}/OAIBreakoutVO.h \
    $${PWD}/OAIClientWorkgroupDetailVO.h \
    $${PWD}/OAIClientWorkgroupExpandVO.h \
    $${PWD}/OAIClientWorkgroupListVO.h \
    $${PWD}/OAIClientWorkgroupSimpleVO.h \
    $${PWD}/OAIContactUserVO.h \
    $${PWD}/OAIContactsListVO.h \
    $${PWD}/OAIContactsSimpleVO.h \
    $${PWD}/OAICountryListVO.h \
    $${PWD}/OAICountryVO.h \
    $${PWD}/OAICustomFieldPersistVO.h \
    $${PWD}/OAIDeactivationReasonListVO.h \
    $${PWD}/OAIDeactivationReasonVO.h \
    $${PWD}/OAIErgoSpecSimpleVO.h \
    $${PWD}/OAIEstimateBaseVO.h \
    $${PWD}/OAIEstimateDetailsVO.h \
    $${PWD}/OAIEstimateExpandVO.h \
    $${PWD}/OAIEstimateItemDetailsVO.h \
    $${PWD}/OAIEstimateItemPO.h \
    $${PWD}/OAIEstimateItemPriceVO.h \
    $${PWD}/OAIEstimateListExpandVO.h \
    $${PWD}/OAIEstimatePO.h \
    $${PWD}/OAIEstimateSimpleVO.h \
    $${PWD}/OAIFileListResponseVO.h \
    $${PWD}/OAIFileResponseVO.h \
    $${PWD}/OAIFileTagResponseVO.h \
    $${PWD}/OAIFileVO.h \
    $${PWD}/OAIHTTPStatusVO.h \
    $${PWD}/OAIInvoiceDetailListExpandVO.h \
    $${PWD}/OAIInvoiceDetailVO.h \
    $${PWD}/OAIInvoiceExpandVO.h \
    $${PWD}/OAIInvoiceItemDetailVO.h \
    $${PWD}/OAIInvoiceItemSimpleVO.h \
    $${PWD}/OAIInvoiceSimpleVO.h \
    $${PWD}/OAIItemOptionVO.h \
    $${PWD}/OAIMultiExchangeRateListVO.h \
    $${PWD}/OAIMultiExchangeRatePersisitVO.h \
    $${PWD}/OAIMultiExchangeRatePersistListVO.h \
    $${PWD}/OAIObjectStateListVO.h \
    $${PWD}/OAIObjectStateSimpleVO.h \
    $${PWD}/OAIOrderDetailBaseVO.h \
    $${PWD}/OAIOrderDetailVO.h \
    $${PWD}/OAIOrderDetailWithIndicatorVO.h \
    $${PWD}/OAIOrderDetailWorkgroupLevelVO.h \
    $${PWD}/OAIOrderExpandWorkgroupLevelVO.h \
    $${PWD}/OAIOrderItemPersistVO.h \
    $${PWD}/OAIOrderItemSimpleVO.h \
    $${PWD}/OAIOrderListVO.h \
    $${PWD}/OAIOrderPO.h \
    $${PWD}/OAIOrderSimpleBaseVO.h \
    $${PWD}/OAIOrderSimpleVO.h \
    $${PWD}/OAIOrderUpdPersistVO.h \
    $${PWD}/OAIOrderVO.h \
    $${PWD}/OAIOrderWorkgroupLevelListVO.h \
    $${PWD}/OAIOrderWorkgroupLevelSimpleVO.h \
    $${PWD}/OAIPaperItemPO.h \
    $${PWD}/OAIPersonVO.h \
    $${PWD}/OAIProductTypeVO.h \
    $${PWD}/OAIProfileImageVO.h \
    $${PWD}/OAIProjectBaseVO.h \
    $${PWD}/OAIProjectCategoryListVO.h \
    $${PWD}/OAIProjectCategorySimpleVO.h \
    $${PWD}/OAIProjectDetailVO.h \
    $${PWD}/OAIProjectExpandVO.h \
    $${PWD}/OAIProjectHomeUserFieldsListVO.h \
    $${PWD}/OAIProjectIdListVO.h \
    $${PWD}/OAIProjectListVO.h \
    $${PWD}/OAIProjectParentVO.h \
    $${PWD}/OAIProjectPatchPO.h \
    $${PWD}/OAIProjectPersistVO.h \
    $${PWD}/OAIProjectSimpleVO.h \
    $${PWD}/OAIProjectStatusListVO.h \
    $${PWD}/OAIProjectStatusSimpleVO.h \
    $${PWD}/OAIProjectTimeCardVO.h \
    $${PWD}/OAIProjectVO.h \
    $${PWD}/OAIPropertyPaAndAttVO.h \
    $${PWD}/OAIPropertyParamListVO.h \
    $${PWD}/OAIPropertyParamSimpleVO.h \
    $${PWD}/OAIPropertyPersistVO.h \
    $${PWD}/OAIQuoteBaseVO.h \
    $${PWD}/OAIQuoteDetailVO.h \
    $${PWD}/OAIQuoteExpandVO.h \
    $${PWD}/OAIQuoteItemDetailVO.h \
    $${PWD}/OAIQuoteListVO.h \
    $${PWD}/OAIQuoteOfWgLevelSimpleVO.h \
    $${PWD}/OAIQuotePriceDetailVO.h \
    $${PWD}/OAIQuotePutPersistVO.h \
    $${PWD}/OAIQuoteSimpleVO.h \
    $${PWD}/OAIRfeBaseVO.h \
    $${PWD}/OAIRfeDetailsVO.h \
    $${PWD}/OAIRfeExpandVO.h \
    $${PWD}/OAIRfeItemOptionVO.h \
    $${PWD}/OAIRfeItemSimpleEXTVO.h \
    $${PWD}/OAIRfeItemSimpleVO.h \
    $${PWD}/OAIRfeListVO.h \
    $${PWD}/OAIRfePO.h \
    $${PWD}/OAIRfeSimpleVO.h \
    $${PWD}/OAIRfeSpecPO.h \
    $${PWD}/OAIRfeSuEstimateSimpleVO.h \
    $${PWD}/OAIRfqBaseVO.h \
    $${PWD}/OAIRfqDetailsVO.h \
    $${PWD}/OAIRfqExpandVO.h \
    $${PWD}/OAIRfqItemBaseVO.h \
    $${PWD}/OAIRfqListVO.h \
    $${PWD}/OAIRfqSimpleVO.h \
    $${PWD}/OAIRfqVO.h \
    $${PWD}/OAIRoleListVO.h \
    $${PWD}/OAIRoleSimpleVO.h \
    $${PWD}/OAIShipmentDetailVO.h \
    $${PWD}/OAIShipmentExpandVO.h \
    $${PWD}/OAIShipmentListVO.h \
    $${PWD}/OAIShipmentLocationPersistVO.h \
    $${PWD}/OAIShipmentLocationPostPersistVO.h \
    $${PWD}/OAIShipmentLocationsPOSTResultVO.h \
    $${PWD}/OAIShipmentLocationsPOSTVO.h \
    $${PWD}/OAIShipmentRequestBaseVO.h \
    $${PWD}/OAIShipmentSimpleVO.h \
    $${PWD}/OAISpecBaseVO.h \
    $${PWD}/OAISpecHTTPStatusVO.h \
    $${PWD}/OAISpecListVO.h \
    $${PWD}/OAISpecPersistVO.h \
    $${PWD}/OAISpecSimpleVO.h \
    $${PWD}/OAISpecSimplestVO.h \
    $${PWD}/OAISpecTemplateDetailVO.h \
    $${PWD}/OAISpecTemplateExpandVO.h \
    $${PWD}/OAISpecTemplateListVO.h \
    $${PWD}/OAISpecTemplateSimpleVO.h \
    $${PWD}/OAISpecTypeFieldsListVO.h \
    $${PWD}/OAISpecTypePersistVO.h \
    $${PWD}/OAISpecTypeVO.h \
    $${PWD}/OAISpecUpdatePersistVO.h \
    $${PWD}/OAISpecVO.h \
    $${PWD}/OAISpecVersionPersistVO.h \
    $${PWD}/OAISupplierWorkgroupBasicVO.h \
    $${PWD}/OAISupplierWorkgroupDetailVO.h \
    $${PWD}/OAISupplierWorkgroupExpandVO.h \
    $${PWD}/OAISupplierWorkgroupListVO.h \
    $${PWD}/OAISupplierWorkgroupSimpleVO.h \
    $${PWD}/OAITagRepoVO.h \
    $${PWD}/OAITagVO.h \
    $${PWD}/OAITaskCreatedVO.h \
    $${PWD}/OAITaskDetailVO.h \
    $${PWD}/OAITaskDetailWorkgroupLevelVO.h \
    $${PWD}/OAITaskExpandVO.h \
    $${PWD}/OAITaskExpandWorkgroupLevelVO.h \
    $${PWD}/OAITaskListVO.h \
    $${PWD}/OAITaskPersistVO.h \
    $${PWD}/OAITaskPriorityListVO.h \
    $${PWD}/OAITaskPriorityVO.h \
    $${PWD}/OAITaskSimpleVO.h \
    $${PWD}/OAITaskStatusListVO.h \
    $${PWD}/OAITaskStatusVO.h \
    $${PWD}/OAITaskTimeCardVO.h \
    $${PWD}/OAITaskTypeListVO.h \
    $${PWD}/OAITaskTypeSimpleVO.h \
    $${PWD}/OAITaskWorkgroupLevelListVO.h \
    $${PWD}/OAITaskWorkgroupLevelSimpleVO.h \
    $${PWD}/OAITeamMemberBaseInfVO.h \
    $${PWD}/OAITeamMemberListVO.h \
    $${PWD}/OAITeamMemberPO.h \
    $${PWD}/OAITeamMemberSimpleVO.h \
    $${PWD}/OAITeamTemplateDetailVO.h \
    $${PWD}/OAITeamTemplateExpandVO.h \
    $${PWD}/OAITeamTemplateItemVO.h \
    $${PWD}/OAITeamTemplateListVO.h \
    $${PWD}/OAITeamTemplateSimpleVO.h \
    $${PWD}/OAITimeCardDetailVO.h \
    $${PWD}/OAITimeCardLineVO.h \
    $${PWD}/OAITimeCardListVO.h \
    $${PWD}/OAITimeCardReceivedDetailVO.h \
    $${PWD}/OAITimeCardSimpleVO.h \
    $${PWD}/OAIUofmSimpleVO.h \
    $${PWD}/OAIUserDetailsExpandVO.h \
    $${PWD}/OAIUserDetailsVO.h \
    $${PWD}/OAIUserFieldsSimpleVO.h \
    $${PWD}/OAIUserPersonVO.h \
    $${PWD}/OAIUserVO.h \
    $${PWD}/OAIV1X1SpecUpdatingPO.h \
    $${PWD}/OAIV1x1InvitedTeamMemberResultsVO.h \
    $${PWD}/OAIV1x1InvitedTeamMemberVO.h \
    $${PWD}/OAIV1x1ProperyPO.h \
    $${PWD}/OAIV1x1ProperyVO.h \
    $${PWD}/OAIV1x1SpecDetailVO.h \
    $${PWD}/OAIV1x1SpecExpandVO.h \
    $${PWD}/OAIV1x1SpecPamAndAttPO.h \
    $${PWD}/OAIV1x1SpecPamAndAttVO.h \
    $${PWD}/OAIWgSpecPrdTypeRegPersistVO.h \
    $${PWD}/OAIWgTaskStatusListVO.h \
    $${PWD}/OAIWgTaskStatusVO.h \
    $${PWD}/OAIWorkgroupAttributeListVO.h \
    $${PWD}/OAIWorkgroupAttributeVO.h \
    $${PWD}/OAIWorkgroupBaseVO.h \
    $${PWD}/OAIWorkgroupDetailVO.h \
    $${PWD}/OAIWorkgroupExpandVO.h \
    $${PWD}/OAIWorkgroupHTTPStatusVO.h \
    $${PWD}/OAIWorkgroupListVO.h \
    $${PWD}/OAIWorkgroupMembersListVO.h \
    $${PWD}/OAIWorkgroupMembersSimpleVO.h \
    $${PWD}/OAIWorkgroupSimpleVO.h \
    $${PWD}/OAIWorkgroupUpdPersistVO.h \
# APIs
    $${PWD}/OAIContactApi.h \
    $${PWD}/OAICountryApi.h \
    $${PWD}/OAIDeactivationReasonApi.h \
    $${PWD}/OAIEstimateApi.h \
    $${PWD}/OAIExchangeRateApi.h \
    $${PWD}/OAIFileApi.h \
    $${PWD}/OAIInvoiceApi.h \
    $${PWD}/OAIMyInfoApi.h \
    $${PWD}/OAIOrderApi.h \
    $${PWD}/OAIProjectApi.h \
    $${PWD}/OAIProjectCategoryApi.h \
    $${PWD}/OAIProjectStatusApi.h \
    $${PWD}/OAIQuoteApi.h \
    $${PWD}/OAIRFEApi.h \
    $${PWD}/OAIRfqApi.h \
    $${PWD}/OAIShipmentApi.h \
    $${PWD}/OAISpecApi.h \
    $${PWD}/OAISpecTemplateApi.h \
    $${PWD}/OAITaskApi.h \
    $${PWD}/OAITeamMemberApi.h \
    $${PWD}/OAITeamMemberRoleApi.h \
    $${PWD}/OAITimeCardApi.h \
    $${PWD}/OAIUserFieldsApi.h \
    $${PWD}/OAIWorkgroupApi.h \
    $${PWD}/OAIWorkgroupMembersApi.h \
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
    $${PWD}/OAIAutomaticInvitationVO.cpp \
    $${PWD}/OAIAutomaticInvitationsListVO.cpp \
    $${PWD}/OAIBreakoutVO.cpp \
    $${PWD}/OAIClientWorkgroupDetailVO.cpp \
    $${PWD}/OAIClientWorkgroupExpandVO.cpp \
    $${PWD}/OAIClientWorkgroupListVO.cpp \
    $${PWD}/OAIClientWorkgroupSimpleVO.cpp \
    $${PWD}/OAIContactUserVO.cpp \
    $${PWD}/OAIContactsListVO.cpp \
    $${PWD}/OAIContactsSimpleVO.cpp \
    $${PWD}/OAICountryListVO.cpp \
    $${PWD}/OAICountryVO.cpp \
    $${PWD}/OAICustomFieldPersistVO.cpp \
    $${PWD}/OAIDeactivationReasonListVO.cpp \
    $${PWD}/OAIDeactivationReasonVO.cpp \
    $${PWD}/OAIErgoSpecSimpleVO.cpp \
    $${PWD}/OAIEstimateBaseVO.cpp \
    $${PWD}/OAIEstimateDetailsVO.cpp \
    $${PWD}/OAIEstimateExpandVO.cpp \
    $${PWD}/OAIEstimateItemDetailsVO.cpp \
    $${PWD}/OAIEstimateItemPO.cpp \
    $${PWD}/OAIEstimateItemPriceVO.cpp \
    $${PWD}/OAIEstimateListExpandVO.cpp \
    $${PWD}/OAIEstimatePO.cpp \
    $${PWD}/OAIEstimateSimpleVO.cpp \
    $${PWD}/OAIFileListResponseVO.cpp \
    $${PWD}/OAIFileResponseVO.cpp \
    $${PWD}/OAIFileTagResponseVO.cpp \
    $${PWD}/OAIFileVO.cpp \
    $${PWD}/OAIHTTPStatusVO.cpp \
    $${PWD}/OAIInvoiceDetailListExpandVO.cpp \
    $${PWD}/OAIInvoiceDetailVO.cpp \
    $${PWD}/OAIInvoiceExpandVO.cpp \
    $${PWD}/OAIInvoiceItemDetailVO.cpp \
    $${PWD}/OAIInvoiceItemSimpleVO.cpp \
    $${PWD}/OAIInvoiceSimpleVO.cpp \
    $${PWD}/OAIItemOptionVO.cpp \
    $${PWD}/OAIMultiExchangeRateListVO.cpp \
    $${PWD}/OAIMultiExchangeRatePersisitVO.cpp \
    $${PWD}/OAIMultiExchangeRatePersistListVO.cpp \
    $${PWD}/OAIObjectStateListVO.cpp \
    $${PWD}/OAIObjectStateSimpleVO.cpp \
    $${PWD}/OAIOrderDetailBaseVO.cpp \
    $${PWD}/OAIOrderDetailVO.cpp \
    $${PWD}/OAIOrderDetailWithIndicatorVO.cpp \
    $${PWD}/OAIOrderDetailWorkgroupLevelVO.cpp \
    $${PWD}/OAIOrderExpandWorkgroupLevelVO.cpp \
    $${PWD}/OAIOrderItemPersistVO.cpp \
    $${PWD}/OAIOrderItemSimpleVO.cpp \
    $${PWD}/OAIOrderListVO.cpp \
    $${PWD}/OAIOrderPO.cpp \
    $${PWD}/OAIOrderSimpleBaseVO.cpp \
    $${PWD}/OAIOrderSimpleVO.cpp \
    $${PWD}/OAIOrderUpdPersistVO.cpp \
    $${PWD}/OAIOrderVO.cpp \
    $${PWD}/OAIOrderWorkgroupLevelListVO.cpp \
    $${PWD}/OAIOrderWorkgroupLevelSimpleVO.cpp \
    $${PWD}/OAIPaperItemPO.cpp \
    $${PWD}/OAIPersonVO.cpp \
    $${PWD}/OAIProductTypeVO.cpp \
    $${PWD}/OAIProfileImageVO.cpp \
    $${PWD}/OAIProjectBaseVO.cpp \
    $${PWD}/OAIProjectCategoryListVO.cpp \
    $${PWD}/OAIProjectCategorySimpleVO.cpp \
    $${PWD}/OAIProjectDetailVO.cpp \
    $${PWD}/OAIProjectExpandVO.cpp \
    $${PWD}/OAIProjectHomeUserFieldsListVO.cpp \
    $${PWD}/OAIProjectIdListVO.cpp \
    $${PWD}/OAIProjectListVO.cpp \
    $${PWD}/OAIProjectParentVO.cpp \
    $${PWD}/OAIProjectPatchPO.cpp \
    $${PWD}/OAIProjectPersistVO.cpp \
    $${PWD}/OAIProjectSimpleVO.cpp \
    $${PWD}/OAIProjectStatusListVO.cpp \
    $${PWD}/OAIProjectStatusSimpleVO.cpp \
    $${PWD}/OAIProjectTimeCardVO.cpp \
    $${PWD}/OAIProjectVO.cpp \
    $${PWD}/OAIPropertyPaAndAttVO.cpp \
    $${PWD}/OAIPropertyParamListVO.cpp \
    $${PWD}/OAIPropertyParamSimpleVO.cpp \
    $${PWD}/OAIPropertyPersistVO.cpp \
    $${PWD}/OAIQuoteBaseVO.cpp \
    $${PWD}/OAIQuoteDetailVO.cpp \
    $${PWD}/OAIQuoteExpandVO.cpp \
    $${PWD}/OAIQuoteItemDetailVO.cpp \
    $${PWD}/OAIQuoteListVO.cpp \
    $${PWD}/OAIQuoteOfWgLevelSimpleVO.cpp \
    $${PWD}/OAIQuotePriceDetailVO.cpp \
    $${PWD}/OAIQuotePutPersistVO.cpp \
    $${PWD}/OAIQuoteSimpleVO.cpp \
    $${PWD}/OAIRfeBaseVO.cpp \
    $${PWD}/OAIRfeDetailsVO.cpp \
    $${PWD}/OAIRfeExpandVO.cpp \
    $${PWD}/OAIRfeItemOptionVO.cpp \
    $${PWD}/OAIRfeItemSimpleEXTVO.cpp \
    $${PWD}/OAIRfeItemSimpleVO.cpp \
    $${PWD}/OAIRfeListVO.cpp \
    $${PWD}/OAIRfePO.cpp \
    $${PWD}/OAIRfeSimpleVO.cpp \
    $${PWD}/OAIRfeSpecPO.cpp \
    $${PWD}/OAIRfeSuEstimateSimpleVO.cpp \
    $${PWD}/OAIRfqBaseVO.cpp \
    $${PWD}/OAIRfqDetailsVO.cpp \
    $${PWD}/OAIRfqExpandVO.cpp \
    $${PWD}/OAIRfqItemBaseVO.cpp \
    $${PWD}/OAIRfqListVO.cpp \
    $${PWD}/OAIRfqSimpleVO.cpp \
    $${PWD}/OAIRfqVO.cpp \
    $${PWD}/OAIRoleListVO.cpp \
    $${PWD}/OAIRoleSimpleVO.cpp \
    $${PWD}/OAIShipmentDetailVO.cpp \
    $${PWD}/OAIShipmentExpandVO.cpp \
    $${PWD}/OAIShipmentListVO.cpp \
    $${PWD}/OAIShipmentLocationPersistVO.cpp \
    $${PWD}/OAIShipmentLocationPostPersistVO.cpp \
    $${PWD}/OAIShipmentLocationsPOSTResultVO.cpp \
    $${PWD}/OAIShipmentLocationsPOSTVO.cpp \
    $${PWD}/OAIShipmentRequestBaseVO.cpp \
    $${PWD}/OAIShipmentSimpleVO.cpp \
    $${PWD}/OAISpecBaseVO.cpp \
    $${PWD}/OAISpecHTTPStatusVO.cpp \
    $${PWD}/OAISpecListVO.cpp \
    $${PWD}/OAISpecPersistVO.cpp \
    $${PWD}/OAISpecSimpleVO.cpp \
    $${PWD}/OAISpecSimplestVO.cpp \
    $${PWD}/OAISpecTemplateDetailVO.cpp \
    $${PWD}/OAISpecTemplateExpandVO.cpp \
    $${PWD}/OAISpecTemplateListVO.cpp \
    $${PWD}/OAISpecTemplateSimpleVO.cpp \
    $${PWD}/OAISpecTypeFieldsListVO.cpp \
    $${PWD}/OAISpecTypePersistVO.cpp \
    $${PWD}/OAISpecTypeVO.cpp \
    $${PWD}/OAISpecUpdatePersistVO.cpp \
    $${PWD}/OAISpecVO.cpp \
    $${PWD}/OAISpecVersionPersistVO.cpp \
    $${PWD}/OAISupplierWorkgroupBasicVO.cpp \
    $${PWD}/OAISupplierWorkgroupDetailVO.cpp \
    $${PWD}/OAISupplierWorkgroupExpandVO.cpp \
    $${PWD}/OAISupplierWorkgroupListVO.cpp \
    $${PWD}/OAISupplierWorkgroupSimpleVO.cpp \
    $${PWD}/OAITagRepoVO.cpp \
    $${PWD}/OAITagVO.cpp \
    $${PWD}/OAITaskCreatedVO.cpp \
    $${PWD}/OAITaskDetailVO.cpp \
    $${PWD}/OAITaskDetailWorkgroupLevelVO.cpp \
    $${PWD}/OAITaskExpandVO.cpp \
    $${PWD}/OAITaskExpandWorkgroupLevelVO.cpp \
    $${PWD}/OAITaskListVO.cpp \
    $${PWD}/OAITaskPersistVO.cpp \
    $${PWD}/OAITaskPriorityListVO.cpp \
    $${PWD}/OAITaskPriorityVO.cpp \
    $${PWD}/OAITaskSimpleVO.cpp \
    $${PWD}/OAITaskStatusListVO.cpp \
    $${PWD}/OAITaskStatusVO.cpp \
    $${PWD}/OAITaskTimeCardVO.cpp \
    $${PWD}/OAITaskTypeListVO.cpp \
    $${PWD}/OAITaskTypeSimpleVO.cpp \
    $${PWD}/OAITaskWorkgroupLevelListVO.cpp \
    $${PWD}/OAITaskWorkgroupLevelSimpleVO.cpp \
    $${PWD}/OAITeamMemberBaseInfVO.cpp \
    $${PWD}/OAITeamMemberListVO.cpp \
    $${PWD}/OAITeamMemberPO.cpp \
    $${PWD}/OAITeamMemberSimpleVO.cpp \
    $${PWD}/OAITeamTemplateDetailVO.cpp \
    $${PWD}/OAITeamTemplateExpandVO.cpp \
    $${PWD}/OAITeamTemplateItemVO.cpp \
    $${PWD}/OAITeamTemplateListVO.cpp \
    $${PWD}/OAITeamTemplateSimpleVO.cpp \
    $${PWD}/OAITimeCardDetailVO.cpp \
    $${PWD}/OAITimeCardLineVO.cpp \
    $${PWD}/OAITimeCardListVO.cpp \
    $${PWD}/OAITimeCardReceivedDetailVO.cpp \
    $${PWD}/OAITimeCardSimpleVO.cpp \
    $${PWD}/OAIUofmSimpleVO.cpp \
    $${PWD}/OAIUserDetailsExpandVO.cpp \
    $${PWD}/OAIUserDetailsVO.cpp \
    $${PWD}/OAIUserFieldsSimpleVO.cpp \
    $${PWD}/OAIUserPersonVO.cpp \
    $${PWD}/OAIUserVO.cpp \
    $${PWD}/OAIV1X1SpecUpdatingPO.cpp \
    $${PWD}/OAIV1x1InvitedTeamMemberResultsVO.cpp \
    $${PWD}/OAIV1x1InvitedTeamMemberVO.cpp \
    $${PWD}/OAIV1x1ProperyPO.cpp \
    $${PWD}/OAIV1x1ProperyVO.cpp \
    $${PWD}/OAIV1x1SpecDetailVO.cpp \
    $${PWD}/OAIV1x1SpecExpandVO.cpp \
    $${PWD}/OAIV1x1SpecPamAndAttPO.cpp \
    $${PWD}/OAIV1x1SpecPamAndAttVO.cpp \
    $${PWD}/OAIWgSpecPrdTypeRegPersistVO.cpp \
    $${PWD}/OAIWgTaskStatusListVO.cpp \
    $${PWD}/OAIWgTaskStatusVO.cpp \
    $${PWD}/OAIWorkgroupAttributeListVO.cpp \
    $${PWD}/OAIWorkgroupAttributeVO.cpp \
    $${PWD}/OAIWorkgroupBaseVO.cpp \
    $${PWD}/OAIWorkgroupDetailVO.cpp \
    $${PWD}/OAIWorkgroupExpandVO.cpp \
    $${PWD}/OAIWorkgroupHTTPStatusVO.cpp \
    $${PWD}/OAIWorkgroupListVO.cpp \
    $${PWD}/OAIWorkgroupMembersListVO.cpp \
    $${PWD}/OAIWorkgroupMembersSimpleVO.cpp \
    $${PWD}/OAIWorkgroupSimpleVO.cpp \
    $${PWD}/OAIWorkgroupUpdPersistVO.cpp \
# APIs
    $${PWD}/OAIContactApi.cpp \
    $${PWD}/OAICountryApi.cpp \
    $${PWD}/OAIDeactivationReasonApi.cpp \
    $${PWD}/OAIEstimateApi.cpp \
    $${PWD}/OAIExchangeRateApi.cpp \
    $${PWD}/OAIFileApi.cpp \
    $${PWD}/OAIInvoiceApi.cpp \
    $${PWD}/OAIMyInfoApi.cpp \
    $${PWD}/OAIOrderApi.cpp \
    $${PWD}/OAIProjectApi.cpp \
    $${PWD}/OAIProjectCategoryApi.cpp \
    $${PWD}/OAIProjectStatusApi.cpp \
    $${PWD}/OAIQuoteApi.cpp \
    $${PWD}/OAIRFEApi.cpp \
    $${PWD}/OAIRfqApi.cpp \
    $${PWD}/OAIShipmentApi.cpp \
    $${PWD}/OAISpecApi.cpp \
    $${PWD}/OAISpecTemplateApi.cpp \
    $${PWD}/OAITaskApi.cpp \
    $${PWD}/OAITeamMemberApi.cpp \
    $${PWD}/OAITeamMemberRoleApi.cpp \
    $${PWD}/OAITimeCardApi.cpp \
    $${PWD}/OAIUserFieldsApi.cpp \
    $${PWD}/OAIWorkgroupApi.cpp \
    $${PWD}/OAIWorkgroupMembersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
