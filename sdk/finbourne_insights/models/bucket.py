# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.608
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_insights.configuration import Configuration


class Bucket(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'start_time': 'datetime',
        'item_count': 'int'
    }

    attribute_map = {
        'start_time': 'startTime',
        'item_count': 'itemCount'
    }

    required_map = {
        'start_time': 'optional',
        'item_count': 'optional'
    }

    def __init__(self, start_time=None, item_count=None, local_vars_configuration=None):  # noqa: E501
        """Bucket - a model defined in OpenAPI"
        
        :param start_time:  The bucket's start time as a DateTimeOffset.
        :type start_time: datetime
        :param item_count:  The number of items in the bucket.
        :type item_count: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_time = None
        self._item_count = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if item_count is not None:
            self.item_count = item_count

    @property
    def start_time(self):
        """Gets the start_time of this Bucket.  # noqa: E501

        The bucket's start time as a DateTimeOffset.  # noqa: E501

        :return: The start_time of this Bucket.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Bucket.

        The bucket's start time as a DateTimeOffset.  # noqa: E501

        :param start_time: The start_time of this Bucket.  # noqa: E501
        :type start_time: datetime
        """

        self._start_time = start_time

    @property
    def item_count(self):
        """Gets the item_count of this Bucket.  # noqa: E501

        The number of items in the bucket.  # noqa: E501

        :return: The item_count of this Bucket.  # noqa: E501
        :rtype: int
        """
        return self._item_count

    @item_count.setter
    def item_count(self, item_count):
        """Sets the item_count of this Bucket.

        The number of items in the bucket.  # noqa: E501

        :param item_count: The item_count of this Bucket.  # noqa: E501
        :type item_count: int
        """

        self._item_count = item_count

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bucket):
            return True

        return self.to_dict() != other.to_dict()
