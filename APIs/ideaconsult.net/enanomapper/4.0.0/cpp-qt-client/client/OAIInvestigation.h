/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInvestigation.h
 *
 * 
 */

#ifndef OAIInvestigation_H
#define OAIInvestigation_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInvestigation : public OAIObject {
public:
    OAIInvestigation();
    OAIInvestigation(QString json);
    ~OAIInvestigation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getChildDocuments() const;
    void setChildDocuments(const OAIObject &_child_documents_);
    bool is__child_documents__Set() const;
    bool is__child_documents__Valid() const;

    QString getAssay() const;
    void setAssay(const QString &assay);
    bool is_assay_Set() const;
    bool is_assay_Valid() const;

    QString getDocumentUuid() const;
    void setDocumentUuid(const QString &document_uuid);
    bool is_document_uuid_Set() const;
    bool is_document_uuid_Valid() const;

    QString getEffectendpoint() const;
    void setEffectendpoint(const QString &effectendpoint);
    bool is_effectendpoint_Set() const;
    bool is_effectendpoint_Valid() const;

    QString getEndpoint() const;
    void setEndpoint(const QString &endpoint);
    bool is_endpoint_Set() const;
    bool is_endpoint_Valid() const;

    QString getEndpointcategory() const;
    void setEndpointcategory(const QString &endpointcategory);
    bool is_endpointcategory_Set() const;
    bool is_endpointcategory_Valid() const;

    double getErr() const;
    void setErr(const double &err);
    bool is_err_Set() const;
    bool is_err_Valid() const;

    QString getErrQualifier() const;
    void setErrQualifier(const QString &err_qualifier);
    bool is_err_qualifier_Set() const;
    bool is_err_qualifier_Valid() const;

    QString getGuidance() const;
    void setGuidance(const QString &guidance);
    bool is_guidance_Set() const;
    bool is_guidance_Valid() const;

    QString getInvestigation() const;
    void setInvestigation(const QString &investigation);
    bool is_investigation_Set() const;
    bool is_investigation_Valid() const;

    QString getLoQualifier() const;
    void setLoQualifier(const QString &lo_qualifier);
    bool is_lo_qualifier_Set() const;
    bool is_lo_qualifier_Valid() const;

    double getLoValue() const;
    void setLoValue(const double &lo_value);
    bool is_lo_value_Set() const;
    bool is_lo_value_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOwnerName() const;
    void setOwnerName(const QString &owner_name);
    bool is_owner_name_Set() const;
    bool is_owner_name_Valid() const;

    QString getPublicname() const;
    void setPublicname(const QString &publicname);
    bool is_publicname_Set() const;
    bool is_publicname_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    QString getReferenceOwner() const;
    void setReferenceOwner(const QString &reference_owner);
    bool is_reference_owner_Set() const;
    bool is_reference_owner_Valid() const;

    QString getReferenceYear() const;
    void setReferenceYear(const QString &reference_year);
    bool is_reference_year_Set() const;
    bool is_reference_year_Valid() const;

    QString getResulttype() const;
    void setResulttype(const QString &resulttype);
    bool is_resulttype_Set() const;
    bool is_resulttype_Valid() const;

    QString getSUuid() const;
    void setSUuid(const QString &s_uuid);
    bool is_s_uuid_Set() const;
    bool is_s_uuid_Valid() const;

    QString getStudyResultType() const;
    void setStudyResultType(const QString &study_result_type);
    bool is_study_result_type_Set() const;
    bool is_study_result_type_Valid() const;

    QString getSubstanceType() const;
    void setSubstanceType(const QString &substance_type);
    bool is_substance_type_Set() const;
    bool is_substance_type_Valid() const;

    QString getTextValue() const;
    void setTextValue(const QString &text_value);
    bool is_text_value_Set() const;
    bool is_text_value_Valid() const;

    QString getTopcategory() const;
    void setTopcategory(const QString &topcategory);
    bool is_topcategory_Set() const;
    bool is_topcategory_Valid() const;

    QString getTypeS() const;
    void setTypeS(const QString &type_s);
    bool is_type_s_Set() const;
    bool is_type_s_Valid() const;

    QString getUnit() const;
    void setUnit(const QString &unit);
    bool is_unit_Set() const;
    bool is_unit_Valid() const;

    QString getUpQualifier() const;
    void setUpQualifier(const QString &up_qualifier);
    bool is_up_qualifier_Set() const;
    bool is_up_qualifier_Valid() const;

    double getUpValue() const;
    void setUpValue(const double &up_value);
    bool is_up_value_Set() const;
    bool is_up_value_Valid() const;

    QString getUpdated() const;
    void setUpdated(const QString &updated);
    bool is_updated_Set() const;
    bool is_updated_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m__child_documents_;
    bool m__child_documents__isSet;
    bool m__child_documents__isValid;

    QString m_assay;
    bool m_assay_isSet;
    bool m_assay_isValid;

    QString m_document_uuid;
    bool m_document_uuid_isSet;
    bool m_document_uuid_isValid;

    QString m_effectendpoint;
    bool m_effectendpoint_isSet;
    bool m_effectendpoint_isValid;

    QString m_endpoint;
    bool m_endpoint_isSet;
    bool m_endpoint_isValid;

    QString m_endpointcategory;
    bool m_endpointcategory_isSet;
    bool m_endpointcategory_isValid;

    double m_err;
    bool m_err_isSet;
    bool m_err_isValid;

    QString m_err_qualifier;
    bool m_err_qualifier_isSet;
    bool m_err_qualifier_isValid;

    QString m_guidance;
    bool m_guidance_isSet;
    bool m_guidance_isValid;

    QString m_investigation;
    bool m_investigation_isSet;
    bool m_investigation_isValid;

    QString m_lo_qualifier;
    bool m_lo_qualifier_isSet;
    bool m_lo_qualifier_isValid;

    double m_lo_value;
    bool m_lo_value_isSet;
    bool m_lo_value_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_owner_name;
    bool m_owner_name_isSet;
    bool m_owner_name_isValid;

    QString m_publicname;
    bool m_publicname_isSet;
    bool m_publicname_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    QString m_reference_owner;
    bool m_reference_owner_isSet;
    bool m_reference_owner_isValid;

    QString m_reference_year;
    bool m_reference_year_isSet;
    bool m_reference_year_isValid;

    QString m_resulttype;
    bool m_resulttype_isSet;
    bool m_resulttype_isValid;

    QString m_s_uuid;
    bool m_s_uuid_isSet;
    bool m_s_uuid_isValid;

    QString m_study_result_type;
    bool m_study_result_type_isSet;
    bool m_study_result_type_isValid;

    QString m_substance_type;
    bool m_substance_type_isSet;
    bool m_substance_type_isValid;

    QString m_text_value;
    bool m_text_value_isSet;
    bool m_text_value_isValid;

    QString m_topcategory;
    bool m_topcategory_isSet;
    bool m_topcategory_isValid;

    QString m_type_s;
    bool m_type_s_isSet;
    bool m_type_s_isValid;

    QString m_unit;
    bool m_unit_isSet;
    bool m_unit_isValid;

    QString m_up_qualifier;
    bool m_up_qualifier_isSet;
    bool m_up_qualifier_isValid;

    double m_up_value;
    bool m_up_value_isSet;
    bool m_up_value_isValid;

    QString m_updated;
    bool m_updated_isSet;
    bool m_updated_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvestigation)

#endif // OAIInvestigation_H
