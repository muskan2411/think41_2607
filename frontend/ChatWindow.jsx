import MessageList from './MessageList';
import UserInput from './UserInput';
import ConversationHistory from './ConversationHistory';

const ChatWindow = () => (
  <div className="flex h-screen">
    <ConversationHistory />
    <div className="flex flex-col flex-1">
      <MessageList />
      <UserInput />
    </div>
  </div>
);

export default ChatWindow;
