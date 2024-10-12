/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIEndpoint_patch_positions_ID.h
 *
 * 
 */

#ifndef OAIEndpoint_patch_positions_ID_H
#define OAIEndpoint_patch_positions_ID_H

#include <QJsonObject>

#include "OAIPosition.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPosition;

class OAIEndpoint_patch_positions_ID : public OAIObject {
public:
    OAIEndpoint_patch_positions_ID();
    OAIEndpoint_patch_positions_ID(QString json);
    ~OAIEndpoint_patch_positions_ID() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPosition getData() const;
    void setData(const OAIPosition &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    bool isSuccess() const;
    void setSuccess(const bool &success);
    bool is_success_Set() const;
    bool is_success_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPosition m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    bool m_success;
    bool m_success_isSet;
    bool m_success_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEndpoint_patch_positions_ID)

#endif // OAIEndpoint_patch_positions_ID_H
