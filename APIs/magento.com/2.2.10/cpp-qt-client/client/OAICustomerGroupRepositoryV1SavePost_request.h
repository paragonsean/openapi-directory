/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomerGroupRepositoryV1SavePost_request.h
 *
 * 
 */

#ifndef OAICustomerGroupRepositoryV1SavePost_request_H
#define OAICustomerGroupRepositoryV1SavePost_request_H

#include <QJsonObject>

#include "OAICustomer_data_group_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomer_data_group_interface;

class OAICustomerGroupRepositoryV1SavePost_request : public OAIObject {
public:
    OAICustomerGroupRepositoryV1SavePost_request();
    OAICustomerGroupRepositoryV1SavePost_request(QString json);
    ~OAICustomerGroupRepositoryV1SavePost_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICustomer_data_group_interface getGroup() const;
    void setGroup(const OAICustomer_data_group_interface &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICustomer_data_group_interface m_group;
    bool m_group_isSet;
    bool m_group_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomerGroupRepositoryV1SavePost_request)

#endif // OAICustomerGroupRepositoryV1SavePost_request_H
