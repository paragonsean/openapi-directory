/**
 * Transportation Laws and Incentives
 * Query our database of federal and state laws and incentives for alternative fuels and vehicles, air quality, fuel efficiency, and other transportation-related topics. This dataset powers the <a href=\"https://afdc.energy.gov/laws\">Federal and State Laws and Incentives</a> on the Alternative Fuels Data Center.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILawsResponse.h
 *
 * 
 */

#ifndef OAILawsResponse_H
#define OAILawsResponse_H

#include <QJsonObject>

#include "OAILaw.h"
#include "OAIMetadata.h"
#include <QJsonValue>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMetadata;
class OAILaw;

class OAILawsResponse : public OAIObject {
public:
    OAILawsResponse();
    OAILawsResponse(QString json);
    ~OAILawsResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getInputs() const;
    void setInputs(const QJsonValue &inputs);
    bool is_inputs_Set() const;
    bool is_inputs_Valid() const;

    OAIMetadata getMetadata() const;
    void setMetadata(const OAIMetadata &metadata);
    bool is_metadata_Set() const;
    bool is_metadata_Valid() const;

    QList<OAILaw> getResult() const;
    void setResult(const QList<OAILaw> &result);
    bool is_result_Set() const;
    bool is_result_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_inputs;
    bool m_inputs_isSet;
    bool m_inputs_isValid;

    OAIMetadata m_metadata;
    bool m_metadata_isSet;
    bool m_metadata_isValid;

    QList<OAILaw> m_result;
    bool m_result_isSet;
    bool m_result_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILawsResponse)

#endif // OAILawsResponse_H
