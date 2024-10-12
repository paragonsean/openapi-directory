/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISubscribedNodeList.h
 *
 * List of subscribed nodes
 */

#ifndef OAISubscribedNodeList_H
#define OAISubscribedNodeList_H

#include <QJsonObject>

#include "OAIRange.h"
#include "OAISubscribedNode.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISubscribedNode;
class OAIRange;

class OAISubscribedNodeList : public OAIObject {
public:
    OAISubscribedNodeList();
    OAISubscribedNodeList(QString json);
    ~OAISubscribedNodeList() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISubscribedNode> getItems() const;
    void setItems(const QList<OAISubscribedNode> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    OAIRange getRange() const;
    void setRange(const OAIRange &range);
    bool is_range_Set() const;
    bool is_range_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISubscribedNode> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    OAIRange m_range;
    bool m_range_isSet;
    bool m_range_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISubscribedNodeList)

#endif // OAISubscribedNodeList_H
