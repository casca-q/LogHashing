// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LogRegistry {
    struct SystemLog {
        string logMessage;
        string logHash;
        uint256 timestamp;
    }

    SystemLog[] public logs;

    function addLog(string memory _message, string memory _hash) public {
        logs.push(SystemLog(_message, _hash, block.timestamp));
    }

    function getLogCount() public view returns (uint256) {
        return logs.length;
    }

    function getLog(uint256 index) public view returns (string memory, string memory, uint256) {
        require(index < logs.length, "Index outside of scope");
        return (logs[index].logMessage, logs[index].logHash, logs[index].timestamp);
    }
}